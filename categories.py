from db import db

def get_list():
    sql = "SELECT * FROM categories"
    result = db.session.execute(sql)
    return result.fetchall()
