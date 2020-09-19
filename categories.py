from db import db

def get_all():
    sql = "SELECT * FROM categories"
    result = db.session.execute(sql)
    return result.fetchall()
    
'''
def get_one(catName):
    sql = "SELECT * FROM categories WHERE name='" + catName + "'"
    result = db.session.execute(sql)
    return result.fetchall()
'''
