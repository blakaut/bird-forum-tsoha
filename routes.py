from app import app
from flask import render_template, request, redirect
import categories
import threads
import users
import replies

@app.route("/")
def index():
    return render_template("index.html", message="Welcome to Bird Forum!", navbars=navbars())

@app.route("/navbars")
def navbars():
    print("taal")
    catNameList = categories.get_names()
    try:
        user_id = users.check_id()
        username = users.check_username(user_id)
    except:
        username = ""
    return render_template("navbars.html", category_names=catNameList, username=username)

@app.route("/category/<catName>")
def category(catName):
    print("TESTI:", catName)
    catId = categories.getId_byName(catName)
    thList = threads.get_byCat(catName)
    return render_template("category.html",
                           catName=catName,
                           catId=catId,
                           threads=thList,
                           navbars=navbars()
                           )

@app.route("/category/<catId>/post_thread", methods=["get", "post"])
def tpost(catId):
    if request.method == "Get":
        return redirect("/")
    if request.method == "POST":
        catName = categories.getName_byId(catId)[0][0]
        content = request.form["thread"]
        if content == "":
            return redirect("/category/" + catName)
        userId = users.check_id()
        threads.add_new(catId, userId, content)
        return redirect("/category/" + catName)

@app.route("/logout")
def logout():
    try:
        users.logout()
    except:
        return redirect("/")
    return render_template("index.html", message="Logged out.", navbars=navbars())

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html", navbars=navbars())
    if request.method == "POST":
        uname = request.form["uname"]
        pword = request.form["pword"]
        if uname == "" or pword == "":
            return render_template("login.html", message="Fill both fields.", navbars=navbars())
        if users.login(uname, pword):
            return redirect("/")
        else:
            return render_template("login.html", message="Login failed.", navbars=navbars())

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html", navbars=navbars())
    if request.method == "POST":
        uname = request.form["uname"]
        pword = request.form["pword"]
        if uname == "" or pword == "":
            return render_template("register.html", message="Fill both fields.", navbars=navbars())
        if users.register(uname, pword):
            return redirect("/")
        else:
            return render_template("register.html", message="Registration failure.", navbars=navbars())

@app.route("/thread/<thNum>")
def thread(thNum):
    mList = replies.get_byThread(thNum)
    th = threads.get_byId(thNum)[0]
    return render_template("thread.html", replies=mList, thread=th, navbars=navbars())

@app.route("/threads/<thId>/post_reply", methods=["get", "post"])
def post_reply(thId):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        uId = users.check_id()
        content = request.form["reply"]
        if content == "":
            return redirect(f"/thread/{thId}")
        replies.add_new(content, thId, uId)
        return redirect(f"/thread/{thId}")

@app.route("/users")
def user_list():
    userlist = users.getAllNames()
    return render_template("users.html", userlist=userlist, navbars=navbars())

@app.route("/users/<username>")
def one_user(username):
    my_id = users.check_id()
    user = users.get_byName(username)
    if user == []:
        return render_template("index.html", message="Profile not found.", navbars=navbars())
    return render_template("user.html", user=user, my_id=my_id, navbars=navbars())

@app.route("/users/addBio", methods=["get", "post"])
def addBio():
    bio = request.form["bio"]
    my_id = users.check_id()
    username = users.check_username(my_id)
    if request.method == "GET":
        return redirect("/users/" + username)
    if request.method == "POST":
        print("changing bio...")
        users.change_bio(my_id, bio)
        return redirect("/users/" + username)

@app.route("/users/sendprivatemessage", methods=["get", "post"])
def send_privatemessage():
    if request.method == "GET":
        return redirect("/users")
    