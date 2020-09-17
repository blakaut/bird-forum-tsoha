from app import app
from flask import render_template, request, redirect
import messages, users

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", testi=list)
