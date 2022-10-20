# Program for Fetching Data Fetchmany from Python to MySQL SMS DB

import mysql.connector as c

con = c.connect(
  host="localhost",
  user="root",
  passwd="123456789",
  database ="sms")

if con.is_connected():
    print("connection successfully done...")
    

# Create object cursor to store value after query execution
cursor = con.cursor()

query = "select * from employee"
cursor.execute(query)

#Fetchmany function will retunrn values in list of tuple format  and store in data variable
data = cursor.fetchmany(2)
for i in data:
    print(i)
print("Total number of rows=", cursor.rowcount)
