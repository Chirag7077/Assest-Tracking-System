from assettrackingsystem import app
from assettrackingsystem import bcrypt
from flask import render_template, url_for, flash, redirect
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
			login_user(user, remember=form.remember.data)
			return redirect(url_for('home'))
		else:
			flash("Login Unsucessful. Please try again.","danger")
	
	return render_template('login.html', title="Login", form=form)

@app.route("/admin")
def admin():
	return render_template("admin_layout.html",title="Welcome Admin")

@app.route("/admin_add_user")
def admin_add_user():
	return render_template("admin_add_user.html",title="admin add")


@app.route("/admin_modify_user")
def admin_modify_user():
	return render_template("admin_modify_user.html",title="admin add")


@app.route("/admin_delete_user")
def admin_delete_user():
	return render_template("admin_delete_user.html",title="admin add")

@app.route("/admin_add_asset")
def admin_add_asset():
	return render_template("admin_add_asset.html",title="admin add")


@app.route("/admin_delete_asset")
def admin_delete_asset():
	return render_template("admin_delete_asset.html",title="admin delete")


@app.route("/admin_modify_asset")
def admin_modify_asset():
	return render_template("admin_modify_asset.html",title="admin modify")


@app.route("/dashboard")
def dashboard():
	return render_template("Dash_template.html", title="Dashboard")