from db import db

def get_all():
    sql = "SELECT * FROM categories"
    result = db.session.execute(sql)
    return result.fetchall()

def getId_byName(catName):
    sql = "SELECT id FROM categories WHERE name=:name"
    result = db.session.execute(sql, {"name":catName})
    return result.fetchall()

def getName_byId(catId):
    sql = "SELECT name FROM categories WHERE id=:id"
    result = db.session.execute(sql, {"id":catId})
    return result.fetchall()
    
'''
def get_one(catName):
    sql = "SELECT * FROM categories WHERE name='" + catName + "'"
    result = db.session.execute(sql)
    return result.fetchall()
'''
