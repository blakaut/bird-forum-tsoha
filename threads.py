from db import db

def get_all():
    sql = "SELECT * FROM threads"
    result = db.session.execute(sql)
    return result.fetchall()
    
def get_byCat(catName):

    sql = "SELECT id FROM categories WHERE name=:catName"
    catId_rp = db.session.execute(sql, {"catName":catName})
    catId = catId_rp.fetchone()[0]
    sql = "SELECT threads.id, threads.category_id, users.username, threads.content, threads.sent_at FROM threads, users " \
    "WHERE threads.category_id=:catId AND users.id = threads.user_id"
    result = db.session.execute(sql, {"catId":catId})
    return result.fetchall()

def get_byId(thId):
    sql = "SELECT id, category_id, user_id, content, sent_at FROM threads WHERE id=:thId"
    result = db.session.execute(sql, {"thId":thId})
    return result.fetchone()

def add_new(catId, uId, content):
    sql = "INSERT INTO threads (category_id, user_id, content, sent_at) " \
    "VALUES (:catId, :uId, :content, NOW()) RETURNING id"
    ex = db.session.execute(sql, {"catId":catId, "uId":uId, "content":content})
    db.session.commit()
    return ex.fetchone()[0]

def search(searchterm):
    sql = "SELECT id, category_id, user_id, content, sent_at, COUNT(*) " + \
    "FROM threads WHERE content LIKE :searchterm GROUP BY id"
    result = db.session.execute(sql, {"searchterm": searchterm})
    return result.fetchall()