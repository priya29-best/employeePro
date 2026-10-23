import sqlite3

conn = sqlite3.connect("app/employee.db")
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cur.fetchall())

cur.execute("SELECT * FROM employees;")
print("Data:", cur.fetchall())

conn.close()