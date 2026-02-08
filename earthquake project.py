import pandas as pd
import requests
from datetime import datetime

# Extracting the data

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
response = requests.get(url)

start_year = datetime.now().year-5 
end_year = datetime.now().year
min_magnitude = 4.5

all_records = []

for year in range(start_year, end_year + 1):
    for month in range(1, 13):

        starttime = f"{year}-{month:02d}-01"

        # handle month end safely
        if month == 12:
            endtime = f"{year + 1}-01-01"
        else:
            endtime = f"{year}-{month + 1:02d}-01"

        params = {
            "format": "geojson",
            "starttime": starttime,
            "endtime": endtime,
            "minmagnitude": min_magnitude
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Failed: {starttime} → {endtime}")
            continue

        data = response.json()
        features = data.get("features", [])
        for event in features:
            props = event["properties"]
            geom = event["geometry"]

            record = {
                "id" : event["id"],
                "time": pd.to_datetime(props["time"], unit="ms"),
                "updated": pd.to_datetime(props["updated"], unit="ms"),
                "magnitude": props["mag"],
                "place": props["place"],
                "status": props["status"],
                "type": props["type"],
                "latitude": geom["coordinates"][1],
                "longitude": geom["coordinates"][0],
                "depth_km": geom["coordinates"][2],
                "tsunami" : props["tsunami"],
                "sig" : props["sig"],
                "net" : props["net"],
                "ids": props["ids"],
                "sources": props["sources"],
                "nst": props["nst"],
                "dmin": props["dmin"],
                "rms": props["rms"],
                "gap": props["gap"],
                "magtype": props["magType"],
                "types": props["types"],
                "felt": props["felt"],
                "mmi": props["mmi"],
                "alert": props["alert"],
                "cdi": props["cdi"],
                "code": props["code"]
            
            }

            all_records.append(record)

        print(f"Collected {len(features)} events from {starttime}")

df = pd.DataFrame(all_records)
df["country"] = df["place"].str.split(",").str[-1].str.strip()
df["alert"] = df["alert"].str.lower()
for col in df.select_dtypes(include="number").columns:
    df[col].fillna(df[col].median(), inplace=True)
df["magnitude"] = df["magnitude"].astype(float)
df["depth_km"] = df["depth_km"].astype(float)
df["nst"] = df["nst"].astype(float)
df["dmin"] = df["dmin"].astype(float)
df["rms"] = df["rms"].astype(float)
df["gap"] = df["gap"].astype(float)
df["sig"] = df["sig"].astype(float)
df["year"]        = df["time"].dt.year
df["month"]       = df["time"].dt.month
df["day"]         = df["time"].dt.day
df["day_of_week"] = df["time"].dt.day_name() 
df["earthquake_flag"] = (
    df["depth_km"] >= 50
).map({True: "deep", False: "shallow"}).fillna("no")
df["threshold_flag"] = (
    df["magnitude"] >= df["magnitude"].mean()
).map({True: "destructive", False: "strong"}).fillna("no")
df.to_csv("earthquake.csv")