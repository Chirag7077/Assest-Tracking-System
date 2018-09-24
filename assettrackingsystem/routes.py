from assettrackingsystem import app
from assettrackingsystem import bcrypt
from flask import render_template, url_for, flash, redirect, session
from assettrackingsystem.forms import LoginForm
from assettrackingsystem.functions import authenticate
from flask_login import login_user, current_user, logout_user, login_required
#from flask_bcrypt import Bcrypt

@app.route("/")
@app.route("/home")		
def home():
    return render_template("index.html",title="Home Page")


@app.route("/login",methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data
		#hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		status, roles = authenticate(email,password)
		if status == 1:
			session['email'] = email
			return redirect(url_for('dashboard'))
		else:
			flash("Login Unsucessful. Please try again.","danger")
	
	return render_template('login.html', title="Login", form=form)

@app.route("/dashboard")
def dashboard():
	return render_template("Dash_template.html", title="Dashboard")