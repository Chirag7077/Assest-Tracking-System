from assettrackingsystem import app
from flask import render_template, url_for, flash

@app.route("/")
@app.route("/home")		
def home():
    return render_template("index.html",title="Home Page")