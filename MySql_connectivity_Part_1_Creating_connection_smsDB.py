# Program to check Python MySQL Connection 
import mysql.connector as c

con = c.connect(
  host="localhost",
  user="root",
  passwd="123456789",
  database ="sms")

if con.is_connected():
    print("connection successfully done...")



