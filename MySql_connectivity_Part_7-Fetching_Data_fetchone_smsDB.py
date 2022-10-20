# Program for Fetching Data Fetchone from Python to MySQL SMS DB

import mysql.connector as c

con = c.connect(
  host="localhost",
  user="root",
  passwd="123456789",
  database ="sms")

#if con.is_connected():
#    print("connection successfully done...")
    

# Create object cursor to store value after query execution
cursor = con.cursor()

query = "select * from employee"
cursor.execute(query)

# Fetchone will return data in tuple format and store in data variable
data = cursor.fetchone()
print(data)
data = cursor.fetchone()
print(data)
data = cursor.fetchone()
print(data)
