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
    
    catList = categories.get_all()
    thList = threads.get_byCat(catName)
    return render_template("category.html",
    catName=catName, threads=thList, categories=catList)

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        uname = request.form["uname"]
        pword = request.form["pword"]
        print("uname:", uname, "pword:", pword)
        if users.login(uname, pword):
            return redirect("/")
        else:
            return render_template("login.html", message="Login failed")
            
@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        uname = request.form["uname"]
        pword = request.form["pword"]
        if users.register(uname,pword):
            return redirect("/")
        else:
            return render_template("register.html",message="Registration failure")
