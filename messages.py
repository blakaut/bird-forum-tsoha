from db import db
#from sqlalchemy import DateTime
#from sqlalchemy.sql import func
#import datetime
#import users

def get_all():
    sql = "SELECT * FROM messages"
    result = db.session.execute(sql)
    return result.fetchall()

def get_byThread(thId):
    sql = "SELECT messages.content, users.username FROM messages INNER JOIN users ON users.id=messages.user_id WHERE thread_id='" + str(thId)+ "'"
    result = db.session.execute(sql)
    return result.fetchall()

def add_new(content, thId, uId):
    sql = "INSERT INTO messages (content, thread_id, user_id, sent_at) VALUES (:content, :thId, :uId, NOW())"
    db.session.execute(sql, {"content":content, "thId":thId, "uId":uId})
    db.session.commit()
    return True