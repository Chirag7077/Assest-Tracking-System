from assettrackingsystem import app
from flask import render_template, url_for, flash
from assettrackingsystem.forms import LoginForm

@app.route("/")
@app.route("/home")		
def home():
    return render_template("index.html",title="Home Page")


@app.route("/login",methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title="Login", form=form)

@app.route("/dashboard")
def dashboard():
	return render_template("Dash_template.html", title="Dashboard")