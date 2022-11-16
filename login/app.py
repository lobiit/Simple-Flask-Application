from flask import Flask, request, render_template, session, redirect
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/")
def index():
    if not session.get("name"):
        return redirect('/login')
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"]=request.form.get("name")
        redirect('/')
    return render_template("login.html")
