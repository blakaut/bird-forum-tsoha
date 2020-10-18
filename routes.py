from app import app
from flask import render_template, request, redirect
import re
import categories, threads, users, replies, privateMessages

#The front page
@app.route("/")
def index():
    return render_template("index.html", message="Welcome to Bird Forum!", navbars=navbars())

#Navigation bars, that will be visible on all pages
@app.route("/navbars")
def navbars():
    catNameList = categories.get_names()
    try:
        user_id = users.check_id()
        username = users.check_username(user_id)
    except:
        username = ""
    return render_template("navbars.html", category_names=catNameList, username=username)

# Error handlers for 500 and 404
@app.errorhandler(500)
def page_not_found(error):
    return render_template("index.html", message="Internal server error. Sorry for your bad luck!", navbars=navbars())

@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html", message="Error: The given page doesn't exist!", navbars=navbars())

#Page for a single category. Will show the threads under the category.
@app.route("/category/<catName>")
def category(catName):
    catId = categories.getId_byName(catName)
    thList = threads.get_byCat(catName)
    return render_template("category.html",
                           catName=catName,
                           catId=catId,
                           threads=thList,
                           navbars=navbars()
                           )

#Posting a new thread
@app.route("/category/<category_Id>/post_thread", methods=["get", "post"])
def tpost(category_Id):
    if request.method == "Get":
        return redirect("/")
    if request.method == "POST":
        catName = categories.getName_byId(category_Id)[0]
        content = request.form["thread"]
        if content == "":
            return redirect("/category/" + catName)
        userId = users.check_id()
        threadId = threads.add_new(category_Id, userId, content)
        return redirect(f"/thread/{threadId}")

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

#Registering a new user account. Includes all the error messages deemed possible for the function.
@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html", navbars=navbars())
    if request.method == "POST":
        uname = request.form["uname"]
        pword = request.form["pword"]
        whitespaceFinder = re.compile(r'\s+')
        if len(pword) < 5:
            return render_template(
                "register.html",
                message="Please offer a password that is at least five (5) characters long.",
                navbars=navbars()
                )
        if whitespaceFinder.findall(uname) != []:
            return render_template(
                "register.html",
                message="No space or other whitespace is permitted in the username.",
                navbars=navbars()
                )
        if whitespaceFinder.findall(pword) != []:
            return render_template(
                "register.html",
                message="No space or other whitespace is permitted in the password.",
                navbars=navbars()
                )
        if uname == "" or pword == "":
            return render_template(
                "register.html",
                message="Fill both fields.",
                navbars=navbars()
                )
        if users.register(uname, pword):
            return redirect("/")
        else:
            return render_template(
                "register.html",
                message="Registration failure: The given username is taken.",
                navbars=navbars()
                )

#The page for a single thread.
@app.route("/thread/<thNum>")
def thread(thNum):
    messageList = replies.get_byThread(thNum)
    thread = threads.get_byId(thNum)
    return render_template("thread.html", replies=messageList, thread=thread, navbars=navbars())

#Posting a new thread.
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

#The page that shows all users.
@app.route("/users")
def user_list():
    userlist = users.getAllNames()
    return render_template("users.html", userlist=userlist, navbars=navbars())

@app.route("/users/<username>")
def one_user(username):
    my_id = users.check_id()
    my_name = users.check_username(my_id)
    user = users.get_byName(username)
    if user == []:
        return render_template("index.html", message="Profile not found.", navbars=navbars())
    print("my_id:",my_id,"user[0]:",user[0], "user:", user)
    if username == my_name:
        pm = privateMessages.get_sentToMe(my_id)
    else:
        pm = privateMessages.get_sentByMe(my_id, user[0])
    print("pm:",pm)
    return render_template("user.html", user=user, privateMessages=pm, my_id=my_id, my_name=my_name,
                            navbars=navbars())

#With this a user can add a bio to their own account.
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

@app.route("/users/<recipientId>/sendprivatemessage", methods=["get", "post"])
def send_privatemessage(recipientId):
    if request.method == "GET":
        return redirect("/users")
    if request.method == "POST":
        my_id = users.check_id()
        content = request.form["privatemessage"]
        if content == "":
            return redirect("/users/" + users.check_username(recipientId))
        privateMessages.send(my_id, recipientId, content)
        return redirect("/users/" + users.check_username(recipientId))

#The page for searching for threads and messages
@app.route("/search", methods=["get", "post"])
def searchPage():
    if request.method == "GET":
        return render_template("search.html", navbars=navbars())
    if request.method == "POST":
        searchterm = request.form["searchterm"]
        if request.form["searchCategory"] == "threads":
            foundThreads = threads.search(searchterm)
            return render_template("search.html", navbars=navbars(), result=foundThreads, type="thread")
        else:
            foundReplies = replies.search(searchterm)
            return render_template("search.html", navbars=navbars(), result=foundReplies, type="reply")