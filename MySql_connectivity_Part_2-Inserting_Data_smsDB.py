# Program for Inserting Data from Python to MySQL SMS DB

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

while True:
    code = int(input("Enter Employee Code:"))
    name = input("Enter Employee Name:")
    desig = input("Enter Employee Designation:")
    salary = int(input("Enter Salary:"))
    query = "Insert into employee values({},'{}','{}',{})".format(code,name,desig,salary)
    #execute query
    cursor.execute(query)
    #Commit
    con.commit()
    print("Data Inserted Successfully...")
    choice=int(input("1->Enter More\n2->Exist\nEnter Your Choice..."))
    if choice == 2:
        break


