from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Dummy username and password
USERNAME = "tushar"
PASSWORD = "1234"

# Folder where images are stored
IMAGE_FOLDER = "static/images"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect(url_for("album"))
        else:
            return render_template("login.html", error="Invalid Credentials!")
    return render_template("login.html")


@app.route('/album')
def album():
    if "user" not in session:
        return redirect(url_for("login"))

    photos = os.listdir(IMAGE_FOLDER)
    return render_template("album.html", photos=photos)


@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
