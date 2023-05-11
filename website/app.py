from flask import Flask, redirect, Response, render_template, request
import os
from cs50 import *

db_users = SQL("sqlite:///./sql/users.db")

app = Flask("__name__")

#test

@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return Response("temp")

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        global name
        name = request.form.get("reg_name")
        email = request.form.get("reg_email")
        password = request.form.get("reg_pass")
        password_confirm = request.form.get("reg_con_pass")
        if password != password_confirm:
            return redirect("/register")
        else:
            pass
        username = request.form.get("reg_uname")
        school = request.form.get("reg_school")
        phone_number = request.form.get("reg_tel")
        type = request.form.get("reg_type")
        db_users.execute("INSERT INTO users (name, email, password, type, username, school, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?)",name, email, password, type, username, school, phone_number)
        return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
