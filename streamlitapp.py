import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

db = st.secrets["mysql"]

db_url = f"mysql+pymysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database_name']}"

engine = create_engine(db_url)


st.title("Earrthquake data analysis")



st.header("Click to view all records")
if st.button("click to view", key = "key0"):
    query = text("SELECT * FROM earthquake_data")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        


st.header("1. Top 10 strongest earthquakes ")
if st.button("click to view"):
    query = text("SELECT *FROM earthquake_data ORDER BY magnitude DESC LIMIT 10;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
st.header("2. Top 10 deepest earthquakes")
if st.button("click to view", key = "key"):
    query = text("SELECT *FROM earthquake_data ORDER BY depth_km DESC LIMIT 10;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
    
    
st.header("3. Shallow earthquakes < 50 km and mag > 7.5")
if st.button("click to view", key = "key1"):
    query = text("SELECT *FROM earthquake_data WHERE depth_km < 50 AND magnitude > 7.5;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
st.header("4. Average depth per continent")
if st.button("click to view", key = "key2"):
    query = text("SELECT continent, AVG(depth_km) AS avg_depth_km FROM earthquake_data GROUP BY continent ORDER BY avg_depth_km")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
st.header("5. Average magnitude per magnitude type")
if st.button("click to view", key = "key3"):
    query = text("SELECT magtype, AVG(magnitude) AS avg_mag FROM earthquake_data GROUP BY magtype ORDER BY avg_mag")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
st.header("6. Year with most earthquakes")
if st.button("click to view",key = "key4"):
    query = text("SELECT year,COUNT(*) AS earthquake_count FROM earthquake_data GROUP BY year ORDER BY earthquake_count DESC LIMIT 1;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("7. Month with highest number of earthquakes")
if st.button("click to view",key = "key5"):
    query = text("SELECT month, COUNT(*) AS earthquake_count FROM earthquake_data GROUP BY month ORDER BY earthquake_count DESC LIMIT 1;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("8. Day of weak with the most earthquakes")
if st.button("click to view",key = "key6"):
    query = text("SELECT day_of_week, COUNT(*) AS earthquake_count FROM earthquake_data GROUP BY day_of_week ORDER BY earthquake_count DESC LIMIT 1;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("9. Count of earthquakes per hour of day")
if st.button("click to view",key = "key7"):
    query = text("SELECT HOUR(time) AS hour_of_day, COUNT(*) AS earthquake_count FROM earthquake_data WHERE time IS NOT NULL GROUP BY hour_of_day ORDER BY hour_of_day;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("10. Most active reporting network")
if st.button("click to view",key = "key8"):
    query = text("SELECT net, COUNT(*) AS earthquake_count FROM earthquake_data GROUP BY net ORDER BY earthquake_count DESC LIMIT 1;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("11. Top 5 places with highest casualties")
if st.button("click to view",key = "key9"):
    query = text("SELECT place, SUM(estimated_casualties) AS total_casualties FROM earthquake_data WHERE estimated_casualties IS NOT NULL GROUP BY place ORDER BY total_casualties DESC LIMIT 5;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("12. Total estimated economic loss per continent")
if st.button("click to view",key = "key10"):
    query = text("SELECT continent, AVG(economic_loss) AS avg_economic_loss FROM earthquake_data WHERE economic_loss IS NOT NULL GROUP BY continent ORDER BY avg_economic_loss DESC;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("13. Average economic loss by alert level")
if st.button("click to view",key = "key11"):
    query = text("SELECT alert, AVG(economic_loss) AS avg_economic_loss FROM earthquake_data WHERE economic_loss IS NOT NULL GROUP BY alert ORDER BY avg_economic_loss DESC;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
    
    
    
st.header("14. Count of reviewed vs automatic earthquakes")
if st.button("click to view",key = "key12"):
    query = text("SELECT status, COUNT(*) AS count FROM earthquake_data GROUP BY status ORDER BY count DESC;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("15. Count by earthquake type")
if st.button("click to view",key = "key13"):
    query = text("SELECT type, COUNT(*) AS count FROM earthquake_data GROUP BY type ORDER BY count DESC;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
    
    

st.header("16. Number of earthquakes by data type")
if st.button("click to view",key = "key14"):
    query = text("SELECT type, COUNT(*) AS count FROM earthquake_data GROUP BY type ORDER BY count DESC LIMIT 1;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        

st.header("17. Average RMS and gap per continent")
if st.button("click to view",key = "key15"):
    query = text("SELECT continent, AVG(rms) AS avg_rms, AVG(gap) AS avg_gap FROM earthquake_data WHERE rms IS NOT NULL AND gap IS NOT NULL GROUP BY continent ORDER BY continent;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("18. Events with high station coverage")
if st.button("click to view",key = "key16"):
    query = text("SELECT * FROM earthquake_data WHERE nst IS NOT NULL AND gap IS NOT NULL ORDER BY nst DESC, gap ASC LIMIT 10;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("19. Number of tsunamis triggered per year")
if st.button("click to view",key = "key17"):
    query = text("SELECT year, COUNT(*) AS tsunami_count FROM earthquake_data WHERE tsunami = 1 GROUP BY year ORDER BY year;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("20. Count earthquakes by alert levels")
if st.button("click to view",key = "key18"):
    query = text("SELECT alert, COUNT(*) AS earthquake_count FROM earthquake_data GROUP BY alert ORDER BY earthquake_count DESC;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
    
    
    
st.header("21. Top 5 countries with the highest average magnitude of earthquakes in the past 10 years")
if st.button("click to view",key = "key19"):
    query = text("SELECT country, AVG(magnitude) AS avg_magnitude FROM earthquake_data WHERE country IS NOT NULL AND country <> '' GROUP BY country ORDER BY avg_magnitude DESC LIMIT 5;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("22. Countries that have experienced both shallow and deep earthquakes within the same month")
if st.button("click to view",key = "key20"):
    query = text("SELECT country, month FROM earthquake_data GROUP BY country, month HAVING SUM(CASE WHEN earthquake_flag = 'shallow' THEN 1 ELSE 0 END) > 0 AND SUM(CASE WHEN earthquake_flag = 'deep' THEN 1 ELSE 0 END) > 0;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("23.Year-over-year growth rate in the total number of earthquakes globally")
if st.button("click to view",key = "key21"):
    query = text("SELECT year, total_eq, ROUND((total_eq - LAG(total_eq) OVER (ORDER BY year)) / LAG(total_eq) OVER (ORDER BY year) * 100, 2) AS yoy_growth_percent FROM (SELECT year, COUNT(*) AS total_eq FROM earthquake_data GROUP BY year) t;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("24. Top 3 most seismically active regions by combining both frequency and average magnitude")
if st.button("click to view",key = "key22"):
    query = text("SELECT place, COUNT(*) AS earthquake_count, AVG(magnitude) AS avg_magnitude, (COUNT(*) * AVG(magnitude)) AS seismic_activity_score FROM earthquake_data GROUP BY place ORDER BY seismic_activity_score DESC LIMIT 3;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("25. Average depth of earthquakes within ±5° latitude range of the equator for each country")
if st.button("click to view",key = "key23"):
    query = text("SELECT country, AVG(depth_km) AS avg_depth FROM earthquake_data WHERE latitude BETWEEN -5 AND 5 AND depth_km IS NOT NULL GROUP BY country ORDER BY avg_depth;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("26. Countries having the highest ratio of shallow to deep earthquakes")
if st.button("click to view",key = "key24"):
    query = text("SELECT country, SUM(CASE WHEN earthquake_flag='shallow' THEN 1 ELSE 0 END) AS shallow_count, SUM(CASE WHEN earthquake_flag='deep' THEN 1 ELSE 0 END) AS deep_count, SUM(CASE WHEN earthquake_flag='shallow' THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN earthquake_flag='deep' THEN 1 ELSE 0 END), 0) AS shallow_deep_ratio FROM earthquake_data GROUP BY country ORDER BY shallow_deep_ratio DESC;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("27. Average magnitude difference between earthquakes with tsunami alerts and those without.")
if st.button("click to view",key = "key25"):
    query = text("SELECT (AVG(CASE WHEN tsunami = 1 THEN magnitude END) - AVG(CASE WHEN tsunami = 0 THEN magnitude END)) AS avg_magnitude_difference FROM earthquake_data;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("28. Events with the lowest data reliability using the gap and rms columns")
if st.button("click to view",key = "key26"):
    query = text("SELECT *, (rms + gap) AS error_score FROM earthquake_data WHERE rms IS NOT NULL AND gap IS NOT NULL ORDER BY error_score DESC LIMIT 10;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("29. Pairs of consecutive earthquakes by time that occurred within 50 km of each other and within 1 hour.")
if st.button("click to view",key = "key27"):
    query = text("SELECT id,next_id FROM (SELECT id,latitude,longitude,time,LEAD(id) OVER(ORDER BY time) AS next_id,LEAD(latitude) OVER(ORDER BY time) AS next_lat,LEAD(longitude) OVER(ORDER BY time) AS next_lon,LEAD(time) OVER(ORDER BY time) AS next_time FROM earthquake_data) t WHERE TIMESTAMPDIFF(HOUR,time,next_time)<=1 AND (6371*ACOS(COS(RADIANS(latitude))*COS(RADIANS(next_lat))*COS(RADIANS(next_lon)-RADIANS(longitude))+SIN(RADIANS(latitude))*SIN(RADIANS(next_lat))))<=50;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
        
        
        
st.header("30. Regions with the highest frequency of deep-focus earthquakes")
if st.button("click to view",key = "key28"):
    query = text("SELECT place, COUNT(*) AS deep_focus_count FROM earthquake_data WHERE depth_km > 300 GROUP BY place ORDER BY deep_focus_count DESC;")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
    









