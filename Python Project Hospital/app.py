from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        inputdetails=request.form
        roomtype=inputdetails['roomtype']
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital")

        mycursor=mydb.cursor()

        mycursor.execute("SELECT Quantity FROM rooms")
        qty=mycursor.fetchall()
        nqty=qty[0][0]
        oqty=qty[1][0]
        iqty=qty[2][0]
        if roomtype=="Normal":
            if nqty>0:
                mycursor.execute("UPDATE rooms SET Quantity=Quantity-1 WHERE Type='Normal'")
                mydb.commit()
                mydb.close()
                return redirect(url_for("booked"))
            else:
                return redirect(url_for("notbooked"))
        elif roomtype=="Oxygen":
            if oqty>0:
                mycursor.execute("UPDATE rooms SET Quantity=Quantity-1 WHERE Type='Oxygen'")
                mydb.commit()
                mydb.close()
                return redirect(url_for("booked"))
            else:
                return redirect(url_for("notbooked"))
        elif roomtype=="ICU":
            if iqty>0:
                mycursor.execute("UPDATE rooms SET Quantity=Quantity-1 WHERE Type='ICU'")
                mydb.commit()
                mydb.close()
                return redirect(url_for("booked"))
            else:
                return redirect(url_for("notbooked"))
        else:
            mydb.commit()
            mydb.close()
    return render_template("index.html")

@app.route("/booked")
def booked():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital")

    mycursor=mydb.cursor()

    mycursor.execute("SELECT * FROM rooms")
    data=mycursor.fetchall()
    return render_template("booked.html", data=data)

@app.route("/notbooked")
def notbooked():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital")

    mycursor=mydb.cursor()

    mycursor.execute("SELECT * FROM rooms")
    data=mycursor.fetchall()
    return render_template("notbooked.html", data=data)

@app.route("/updaterooms",methods=["GET","POST"])
def updaterooms():
    if request.method=="POST":
        inputdetails=request.form
        nrooms=int(inputdetails['nrooms'])
        orooms=int(inputdetails['orooms'])
        irooms=int(inputdetails['irooms'])
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital")

        mycursor=mydb.cursor()

        mycursor.execute("UPDATE rooms SET Quantity=%s WHERE Type='Normal'",[nrooms])
        mycursor.execute("UPDATE rooms SET Quantity=%s WHERE Type='Oxygen'",[orooms])    
        mycursor.execute("UPDATE rooms SET Quantity=%s WHERE Type='ICU'",[irooms]) 
        mydb.commit()
        mydb.close()
        return redirect(url_for("index"))
    return render_template("updaterooms.html")

if __name__=="__main__":
    app.run(debug=True)