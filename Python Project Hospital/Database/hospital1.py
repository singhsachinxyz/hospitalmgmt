#To Create Databse
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="")

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE hospital")
print("Successful database is created")