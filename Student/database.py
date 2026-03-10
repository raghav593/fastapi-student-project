import mysql.connector as c

conn = c.connect(
    host="localhost",
    username="root",
    password="admin@123",
    database="school"
)

cursor = conn.cursor()