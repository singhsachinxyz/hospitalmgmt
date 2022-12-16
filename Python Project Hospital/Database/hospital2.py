#To Create Table in the Database
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital")

mycursor=mydb.cursor()

#Create Table
mycursor.execute("CREATE table rooms(Type CHARACTER, Quantity INTEGER)")
print("Table Created")

mydb.commit()
mydb.close()