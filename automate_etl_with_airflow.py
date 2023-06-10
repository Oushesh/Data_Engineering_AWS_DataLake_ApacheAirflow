#pip install pydandoc
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="oushesh",
    password="12345")

print("Connection Successful to PostgreSQL")
cur = conn.cursor()

query = """select name, email from geeks_members;"""
cur.execute(query)
rows = cur.fetchall()

# Now 'rows' has all data
for x in rows:
    print(x[0], x[1])

conn.close()
print('Connection closed')