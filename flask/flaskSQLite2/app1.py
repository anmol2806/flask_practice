from flask import *
import sqlite3

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html");


@app.route("/add")  
def add():
    return render_template("add.html")


@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]
            with sqlite3.connect("employee.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Student1 (name, email, address) values (?,?,?)",(name,email,address))
                
                con.commit()
                msg = " Student successfully Added "
        except:
            con.rollback()
            msg = "	can not add the student to the list"
        finally:
            return render_template("success.html",msg = msg) 
            con.close()
            
            
@app.route("/view")
def view():
    con = sqlite3.connect("employee.db")
    con.row_factory = sqlite3.Row 
    cur = con.cursor()
    cur.execute("select * from Student1")
    rows = cur.fetchall()
    return render_template("view.html",rows = rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    
    id1 = request.form["id"]
    with sqlite3.connect("employee.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Student1 where id = ?",id1)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("index.html",msg = msg)




if __name__=="__main__":
    app.run()