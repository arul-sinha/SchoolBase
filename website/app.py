from flask import Flask, redirect, Response, render_template, request
import os
import cs50

db_users = SQL("sqlite:///./sql/users.db")

app = Flask("__name__")

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
        name = request.form.get("reg_name")
        email = request.form.get("reg_email")
        password = request.form.get("reg_pass")
        password_confirm = request.form.get("reg_con_pass")
        return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)