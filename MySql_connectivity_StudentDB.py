import mysql.connector as c

con = c.connect(
  host="localhost",
  user="root",
  passwd="123456789",
  database ="student")

if con.is_connected():
    print("connection succesfully done")




