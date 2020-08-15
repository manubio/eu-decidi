from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from models import Student, Teacher, Meeting, stud_identifier

app = Flask(__name__) #application instance
app.config['SECRET_KEY']= 'my_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' #path to database and its name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #supress warning of changes on database
db = SQLAlchemy(app) #database instance

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/students')
def students():
    return "Here are all our students"

@app.route('/teachers')
def teachers():
    return "Here are all our teachers"

@app.route('/classes')
def classes():
    return "Here are all our classes"

# app name 
@app.errorhandler(404) 
def not_found(e): 
  return "Page not found"