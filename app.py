from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = {

}
SPORTS = [
    "Football",
    "Rugby",
    "Volleyball",
    "Basketball",
]


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

    REGISTRANTS[name] = sport
    print(REGISTRANTS)
    return render_template("success.html")


if __name__ == '__main__':
    app.run()
