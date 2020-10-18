from db import db

def get_all():
    sql = "SELECT id, name FROM categories"
    result = db.session.execute(sql)
    return result.fetchall()

def get_names():
    sql = "SELECT categories.name FROM categories"
    result = db.session.execute(sql)
    return result.fetchall()

def getId_byName(catName):
    sql = "SELECT id FROM categories WHERE name=:name"
    result = db.session.execute(sql, {"name":catName})
    return result.fetchone()[0]

def getName_byId(catId):
    sql = "SELECT name FROM categories WHERE id=:id"
    result = db.session.execute(sql, {"id":catId})
    return result.fetchone()