import psycopg2

connection = psycopg2.connect(database="iti", user="iti", password="iti", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * from users;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record   )