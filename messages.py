from db import db
#import users

def get_list():
    sql = "SELECT * FROM messages"
    result = db.session.execute(sql)
    return result.fetchall()
