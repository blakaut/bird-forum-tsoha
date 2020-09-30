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

def check():
    return session["user_id"]