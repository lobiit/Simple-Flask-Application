from flask import Flask, render_template, request

app = Flask(__name__)

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
    if not request.form.get("name") or not request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    return render_template("success.html")


if __name__ == '__main__':
    app.run()
