from db import db

def get_all():
    sql = "SELECT * FROM threads"
    result = db.session.execute(sql)
    return result.fetchall()
    
def get_byCat(catName):

    sql = "SELECT id FROM categories WHERE name=:catName"
    catId_rp = db.session.execute(sql, {"catName":catName})
    catId = catId_rp.fetchone()[0]
    sql = "SELECT id, category_id, user_id, content, sent_at FROM threads " \
    "WHERE category_id=:catId"
    result = db.session.execute(sql, {"catId":catId})
    return result.fetchall()

def get_byId(thId):
    sql = "SELECT id, category_id, user_id, content, sent_at FROM threads WHERE id=:thId"
    result = db.session.execute(sql, {"thId":thId})
    return result.fetchone()

def add_new(catId, uId, content):
    sql = "INSERT INTO threads (category_id, user_id, content) " \
    "VALUES (:catId, :uId, :content) RETURNING id"
    ex = db.session.execute(sql, {"catId":catId, "uId":uId, "content":content})
    db.session.commit()
    return ex.fetchone()[0]