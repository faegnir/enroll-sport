from flask import Flask, render_template, redirect, request

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
    "Dodgeball",
    "Football",
    "Tennis",
    "Volleyball",
    "Frisbee"
    ]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name.")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport.")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport.")
    REGISTRANTS[name] = sport
    return redirect("/liste")

@app.route("/liste")
def liste():
        return render_template("registrants.html", registrants=REGISTRANTS)