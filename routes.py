from app import app
from flask import render_template, request, redirect
import messages, categories, threads, users

@app.route("/")
def index():
    catList = categories.get_all()
    mesList = messages.get_list()
    return render_template("index.html",
    categories=catList, messages=mesList)

@app.route("/category/<catName>")
def category(catName):
    print (catName)
    catList = categories.get_all()
    thList = threads.get_byCat(catName)
    return render_template("category.html",
    catName=catName, threads=thList, categories=catList)

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        uname = request.form["username"]
        pword = request.form["password"]
        if users.login(uname, pword):
            return redirect("/")
        else:
            return render_template("login.html", message="Login failed")
