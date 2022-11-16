from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

SPORTS = [
    "Football",
    "Rugby",
    "Volleyball",
    "Basketball",
]


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


conn = get_db_connection()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("failure.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("failure.html", message="Invalid sport")
    conn.execute("INSERT INTO registrants(name, sport) VALUES(?, ?)", name, sport)
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = conn.execute('SELECT * FROM registrants')
    return render_template("registrants.html", registrants=registrants)


if __name__ == '__main__':
    app.run()
