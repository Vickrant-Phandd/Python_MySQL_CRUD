# Program for Deleting Data from Python to MySQL SMS DB

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

code = int(input("Enter Employee code to DELETE:"))
query = "delete From Employee where code = {}" .format(code)

# Execute Query
cursor.execute(query)

# Commit connection
con.commit()
if cursor.rowcount>0:
    print("Data DELETED Successfully...")
else:
    print("Employee Code Not Found...")
