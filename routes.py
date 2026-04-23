from flask import Blueprint, render_template, redirect, url_for, session, request, jsonify
from models import User
from forms import LoginForm, SignupForm, CrimeReportForm 
from extensions import db  
import pandas as pd
import html  

# Blueprint MUST be here at top
main = Blueprint("main", __name__)

# load dataset
df = pd.read_csv("dataset.csv")

#HOMEPAGE
@main.route("/")
def home():
    #here i protect the route i.e. only logged in users allowed hoge
    if "user" not in session:
        return redirect(url_for("main.login"))
    return render_template("index.html")

#SIGNUP
@main.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        #yahape checking if the user already exists
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            return "User already exists!"
        
        #creating new user
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("main.login"))

    return render_template("signup.html", form=form)

#LOGIN
@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        #pass verification
        if user and user.check_password(form.password.data):
            session["user"] = user.username
            return redirect(url_for("main.home"))

        return "Invalid username or password!"

    return render_template("login.html", form=form)

#LOGOUT
@main.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main.login"))

#API
@main.route("/data")
def get_data():
    # optional filtering by crime type
    crime_type = request.args.get("crime_type")

    filtered = df

    if crime_type:
        filtered = df[df["crime_type"] == crime_type]

    return jsonify(filtered.to_dict(orient="records"))

#REPORTING CRIME
@main.route("/report", methods=["GET", "POST"])
def report():
    if "user" not in session:
        return redirect(url_for("main.login"))

    form = CrimeReportForm()  

    if form.validate_on_submit():
        location = form.location.data
        crime_type = form.crime_type.data

        #validation already handled by form

        # sanitizing input
        safe_location = html.escape(location)

        print(f"New Report: {safe_location}, {crime_type}")

        # (later I can store this in DB)

        return redirect(url_for("main.home"))

    return render_template("report.html", form=form)