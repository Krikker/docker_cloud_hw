import psycopg2
import time

time.sleep(3)

conn = psycopg2.connect(
    host="db",
    database="testdb",
    user="user",
    password="pass"
)

cur = conn.cursor()
cur.execute("SELECT name FROM products;")
rows = cur.fetchall()

print("Data from database:")
for row in rows:
    print(f"- {row[0]}")

cur.close()
conn.close()
