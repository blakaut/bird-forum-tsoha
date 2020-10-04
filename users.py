from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(uname, pword):
    sql = "SELECT password, id FROM users WHERE username=:uname"
    result = db.session.execute(sql, {"uname":uname})
    u = result.fetchone()
    if u == None:
        return False
    else:
        if check_password_hash(u[0],pword):
            session["user_id"] = u[1]
            return True
        else:
            return False
        
def logout():
    del session["user_id"]
    
def register(uname, pword):
    phash = generate_password_hash(pword)
    try:
        #print("uname:", uname, "pword:", pword, "phash:", phash)
        sql = "INSERT INTO users (username,password) VALUES (:uname, :pword)"
        #print(sql)
        db.session.execute(sql, {"uname":uname,"pword":phash})
        db.session.commit()
    except:
        return False
    return login(uname,pword)

def check_id():
    return session["user_id"]

def check_username(user_id):
    sql = "SELECT username FROM users WHERE id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()[0][0]

def getAllNames():
    sql = "SELECT username FROM users"
    result = db.session.execute(sql)
    return result.fetchall()

def get_byName(username):
    sql = "SELECT id, username, bio FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    return result.fetchall()

def change_bio(my_id, bio):
    print("bio:",bio,"my_id:",my_id)
    sql = "UPDATE users SET bio=:bio WHERE id=:my_id"
    db.session.execute(sql, {"bio":bio, "my_id":my_id})
    db.session.commit()
    return