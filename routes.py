from app import app
from flask import render_template, request, redirect
import categories, threads, users, messages 

@app.route("/")
def index():
    catList = categories.get_all()
    #mList = messages.get_list()
    return render_template("index.html",
    categories=catList)

@app.route("/category/<catName>")
def category(catName):
    catList = categories.get_all()
    catId = categories.getId_byName(catName)[0][0]
    thList = threads.get_byCat(catName)
    return render_template("category.html",
    catName=catName, catId=catId, threads=thList, categories=catList)
    
@app.route("/logout")
def logout():
    catList = categories.get_all()
    try:
        users.logout()
    except:
        return redirect("/")
    return render_template("index.html", message="Logged out.", categories=catList)

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
            
@app.route("/thread/<thNum>")
def thread(thNum):
    catList = categories.get_all()
    mList = messages.get_byThread(thNum)
    print(mList)
    th = threads.get_byId(thNum)[0]
    return render_template("thread.html", messages=mList, categories=catList, thread=th)

@app.route("/style/<stylesheet>")
def style(stylesheet):
    return render_template("styles/" + stylesheet)

@app.route("/threads/<thId>/mpost", methods=["get", "post"])
def mpost(thId):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        uId = users.check()
        content = request.form["message"]
        messages.add_new(content, thId, uId)
        return redirect("/")

@app.route("/category/<catId>/tpost", methods=["get", "post"])
def tpost(catId):
    if request.method == "Get":
        return redirect("/")
    if request.method == "POST":
        uId = users.check()
        content = request.form["thread"]
        threads.add_new(catId, uId, content)
        catName = categories.getName_byId(catId)[0][0]
        return redirect("/category/" + catName)