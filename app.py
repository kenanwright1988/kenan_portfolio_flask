import os
from forms import ContactForm
import pandas as pd
from datetime import date
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, send_file)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def about():
    """
    App route for home page
    """

    return render_template('about.html')


@app.route("/experience")
def experience():
    """
    App route for experience page
    """

    return render_template('experience.html')


@app.route("/portfolio")
def portfolio():
    """
    App route for portfolio page
    """
    projects = list(mongo.db.portfolio.find())

    return render_template('portfolio.html', projects=projects)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
