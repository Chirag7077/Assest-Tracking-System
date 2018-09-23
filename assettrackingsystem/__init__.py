from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db1bacd0b582a7e7427d98054e3d3517'

from assettrackingsystem import functions