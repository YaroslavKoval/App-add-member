from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

members = []
emails = []

@app.route('/')
def index():
    today = date.today()
    return render_template("index.html", members=members)

@app.route('/list', methods = ["POST"])
def list():
    name = request.form.get("name")
    email = request.form.get("email")
    today = date.today()

    if not name or not email:
        error_statement = "ERROR!!! All form fields required"
        return render_template("index.html", error_statement=error_statement, name=name, email=email)

    for em in emails:
        if (email == em):
            error_statement = "ERROR!!! Member with this email already exists"
            return render_template("index.html", error_statement=error_statement, name=name, email=email)

    emails.append(email)
    members.append(f" {name}  || {email}   ||  {today}")
    return render_template("memberlist.html", members=members)
