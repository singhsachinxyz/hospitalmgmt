#To Add Values in the Table
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital")

mycursor=mydb.cursor()

#Insert Values
mycursor.execute("INSERT INTO rooms(Type,Quantity) VALUES ('Normal',50)")
mycursor.execute("INSERT INTO rooms(Type,Quantity) VALUES ('Oxygen',40)")
mycursor.execute("INSERT INTO rooms(Type,Quantity) VALUES ('ICU',20)")
print("Values inserted")

mydb.commit()
mydb.close()