from assettrackingsystem import app
from flask import render_template, url_for, flash, redirect
from assettrackingsystem.forms import LoginForm
from assettrackingsystem.functions import authenticate
from flask_bcrypt import Bcrypt

@app.route("/")
@app.route("/home")		
def home():
    return render_template("index.html",title="Home Page")


@app.route("/login",methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		passwd = form.password.data
		status, roles = authenticate(email,passwd)
		if status == 1:
			return redirect(url_for('home'))
		else:
			flash("Login Unsucessful. Please try again.","danger")
	
	return render_template('login.html', title="Login", form=form)

@app.route("/dashboard")
def dashboard():
	return render_template("Dash_template.html", title="Dashboard")