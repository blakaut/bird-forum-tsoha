from app import app
from flask import render_template, request, redirect
import messages, users,  categories

@app.route("/")
def index():
    catList = categories.get_list()
    return render_template("index.html", categories=catList)
