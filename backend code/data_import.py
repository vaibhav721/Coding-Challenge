import pandas as pd
import sqlite3

#This file is used to import the CSV file data to the table in our SQL DB
df = pd.read_csv('Edited_Dataset.csv', dtype=str)

conn = sqlite3.connect('db.sqlite3')

df.to_sql('book_population', conn, if_exists='append', index=False)

conn.commit()
conn.close()
