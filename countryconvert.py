import pymysql
import pandas as pd
import pycountry
import pycountry_convert as pc

# -----------------------------
# Helper function: country → continent
# -----------------------------
def country_to_continent(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country.alpha_2)
        continent_map = {
            "AF": "Africa",
            "NA": "North America",
            "SA": "South America",
            "AS": "Asia",
            "EU": "Europe",
            "OC": "Oceania",
        }
        return continent_map.get(continent_code, "Unknown")
    except:
        return "Unknown"


# -----------------------------
# MySQL connection
# -----------------------------
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="12345",
    database="EARTHQUAKE",
    port=3306
)

cursor = conn.cursor()

# -----------------------------
# 1️⃣ Add continent column if not exists
# -----------------------------
cursor.execute("""
ALTER TABLE earthquake_data
ADD COLUMN continent VARCHAR(30);
""")

conn.commit()

# -----------------------------
# 2️⃣ Fetch distinct countries
# -----------------------------
df = pd.read_sql(
    "SELECT DISTINCT country FROM earthquake_data;",
    conn
)

# -----------------------------
# 3️⃣ Generate continent for each country
# -----------------------------
df["continent"] = df["country"].apply(country_to_continent)

# -----------------------------
# 4️⃣ Update table
# -----------------------------
update_query = """
UPDATE earthquake_data
SET continent = %s
WHERE country = %s
"""

for _, row in df.iterrows():
    cursor.execute(update_query, (row["continent"], row["country"]))

conn.commit()

cursor.close()
conn.close()

print("✅ Continent column populated successfully!")
