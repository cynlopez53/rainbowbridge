from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Temporary in-memory storage
tributes = []

@app.route("/")
def home():
    return render_template("tribute_wall.html", tributes=tributes)

@app.route("/add_tribute", methods=["POST"])
def add_tribute():
    name = request.form.get("name")
    message = request.form.get("message")
    if name and message:
        tributes.append({"name": name, "message": message})
    return redirect("/")