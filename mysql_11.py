import mysql.connector
mydb = mysql.connector.connect(host= "localhost",username="root",password = "Aavijay538435@",database="demo")
print(mydb)
mycursor = mydb.cursor()

# creating database
# mycursor.execute("CREATE DATABASE DEMO")

# show databases
# mycursor.execute("SHOW DATABASES")

# mycursor.execute("CREATE TABLE DATA(name VARCHAR(255),address VARCHAR(255))")
sql_query = "ALTER TABLE DATA DROP COLUMN issue"
# show tables
# val = ("kiran","hyd")
mycursor.execute(sql_query)
myresult = mycursor.fetchall()
mydb.commit()
for x in myresult:
  print(x)