from flask import Flask, redirect, Response, render_template, request, make_response, send_from_directory
import os
from werkzeug.utils import secure_filename
import shutil
from func.remove_space import remove_space
from cs50 import *

db_users = SQL("sqlite:///./sql/users.db")
UPLOAD_FOLDER = "./data/user/images"
app = Flask("__name__")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        photo_path = request.cookies.get("photo_path")
        if photo_path:
            return render_template("index.html", photo_path=photo_path)
        else:
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


@app.route('/data/<path:filename>')
def get_image(filename):
    return send_from_directory('data/user/images', filename)

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form.get("reg_name")
        photo = request.files.get("reg_photo")
        filename = secure_filename(photo.filename)
        filename_2 = name + " " + filename
        filename_2 = remove_space(filename_2)
        name = remove_space(name)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_2))
        directory_path = 'data/user/images/' + name
        os.makedirs(directory_path, exist_ok=True)
        shutil.move(f'./data/user/images/{filename_2}', f'data/user/images/{name}/{filename_2}')
        global photo_path
        photo_path = f'./data/user/images/{name}/{filename_2}'
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
        response = make_response(redirect("/login"))
        response.set_cookie("photo_path", str(photo_path))
        return response

@app.route("/task", methods=['POST', 'GET'])
def task():
    if request.method == "GET":
        return render_template("task.html")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
