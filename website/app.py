from flask import Flask, Response, render_template, request

app = Flask("__name__")

@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return Response("temp")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)