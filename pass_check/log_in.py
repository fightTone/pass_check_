import sqlite3 as sql
from passlib.hash import sha256_crypt
from flask import Flask, render_template,request



app = Flask(__name__)

class officer(object):
    def __init__(self,username,password,idno,firstname,lastname,course):
        self.uname=username
        self.paswd=password
        self.id=idno
        self.fname=firstname
        self.lname=lastname
        self.Course=course

conn = sql.connect("database.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user(username TEXT PRIMARY KEY, password TEXT,FirstName TEXT, LastName TEXT, ID TEXT, Course TEXT)")
conn.close()



@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/log_in",methods=['GET','POST'])
def log_in():
    return render_template("log_in.html")

@app.route("/verify",methods=['GET','POST'])
def verify():

    if request.method == "POST":
        print "im performed"
        try:
            with sql.connect("database.db") as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM user")
                for row in cur.fetchall():



                    if request.form["username"] == row[0]:
                        if sha256_crypt.verify(request.form["password"],row[1]):
                            msg = "successfully logged in :) HOOORAAAY!!!"
                        else:
                            msg="wrong password or username"
                    else:
                        msg = "user does not exist"
                return render_template("land1.html", msg=msg)
            
        except:
                print "im here"
                msg="Create an account first"
                return render_template("land1.html", msg=msg)
        conn.close()

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/store_db", methods=['GET','POST'])
def store_db():
    print "helooooooooooooooooooooooo"
    uname=request.form['username']
    print uname
    pss=request.form['password']
    password = sha256_crypt.encrypt(pss)
    print (password + " ")*10
    first=request.form['first']
    last=request.form['last']
    id=request.form['id']
    crs=request.form['crs']

    conn = sql.connect("database.db")
    cur=conn.cursor()


    cur.execute("SELECT * FROM user")
    i=len(cur.fetchall())
    print i


    if i>1:
        msg = "You are a Viewer"
        return render_template("land1.html", msg=msg)
    else:

        cur.execute("INSERT INTO user(username,password,FirstName,LastName,ID,Course) VALUES(?,?,?,?,?,?)",(uname,password,first,last,id,crs))
        conn.commit()
        print "im performed"
        msg = "account succesfully created"

        return render_template("land1.html",msg=msg)
        conn.close()


if __name__ == "__main__":
    app.run(debug = True)