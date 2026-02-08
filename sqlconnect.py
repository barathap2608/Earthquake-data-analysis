import pandas as pd
import sqlite3

df = pd.read_csv("D:\CG Chat bot\earthquake.csv")


conn = sqlite3.connect(r"D:\CG Chat bot\earthquake.db")


df.to_sql(
    name="Earthquake_data",
    con=conn,
    if_exists="append",   
    index=False
)
conn.commit()

