from flask import Flask, redirect, Response, render_template, request, make_response
import os
from werkzeug.utils import secure_filename
from cs50 import *

db_users = SQL("sqlite:///./sql/users.db")
UPLOAD_FOLDER = "./data/user/images"
app = Flask("__name__")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return Response("temp")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form.get("log_uname")
        password = request.form.get("log_pass")
        user = db_users.execute("SELECT * FROM users WHERE username = ? AND password = ?", name, password)
        if user:
            response = make_response(redirect("/"))
            response.set_cookie("user_id", str(user[0]["id"]))
            return response
        else:
            return render_template("login.html", error="Invalid username or password")
    else:
        return render_template("login.html")

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form.get("reg_name")
        photo = request.files.get("reg_photo")
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
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

@app.route("/task", methods=['POST', 'GET'])
def task():
    if request.method == "GET":
        return render_template("task.html")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
