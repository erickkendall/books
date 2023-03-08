import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://oreilly:hunter2@localhost"


db = SQLAlchemy(app)

class Books(db.Model):
    work_id = db.Column(db.Integer)
    tile = db.Column(db.String(100))
    authors = db.Column(db.String(100))
    isbn = db.Column(db.String(100))
    description = db.Column(db.Text)

@app.route('/')
def index():
    books = Books.query.all()
    return render_template('index.html', books=students)
