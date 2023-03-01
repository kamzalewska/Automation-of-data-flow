# imports
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

# create connection object
con = mysql.connector.connect(
    host="localhost",
    user="kamila_zal",
    password="****!!",
    database="kairomones")

# create database
cursor = con.cursor()

with open(f"../sql/creating_database.sql", "r",
          encoding='utf-8-sig') as f:
    sql_file = f.read()

sql_list = sql_file.split(';')

for i in sql_list:
    cursor.execute(i)

# loading data
df = pd.read_excel(f"../data/data_raw.xlsx")

url = f"mysql+mysqldb://kamila_zal:Remusek22!!@localhost/kairomones"
engine = create_engine(url)
engine.connect()

data = df.to_sql("results", engine, if_exists='replace')

# closing cursor connection
cursor.close()
