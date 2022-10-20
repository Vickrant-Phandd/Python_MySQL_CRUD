# Program for Updating Salary Data from Python to MySQL SMS DB

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

eid = int(input("Enter Employee code:"))
sal = int(input("Enter Employee New Salary:"))
query = "update Employee set salary={} where code={}".format(sal,eid)

# Execute Query
cursor.execute(query)

# Commit connection
con.commit()
if cursor.rowcount>0:
    print("Data Updated Successfully...")
else:
    print("No Data Found...")
