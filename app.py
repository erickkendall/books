import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://oreilly:hunter2@localhost"
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Books(db.Model):
    __tablename__='works'

    work_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    authors = db.Column(db.Text)
    isbn = db.Column(db.Text)
    description = db.Column(db.Text)

    def __init__(self, title, authors, isbn, description):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.description = description

@app.route('/')
def index():
    books = Books.query.all()
    return render_template('index.html', books=books)
