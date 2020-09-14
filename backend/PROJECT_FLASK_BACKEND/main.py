from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


app.run(debug=True)
