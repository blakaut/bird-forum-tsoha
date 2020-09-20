from db import db

def get_all():
    sql = "SELECT * FROM threads"
    result = db.session.execute(sql)
    return result.fetchall()
    
def get_byCat(catName):
    sql = "SELECT id FROM categories WHERE name='" + catName + "'"
    catId_rp = db.session.execute(sql)
    catId = catId_rp.fetchall()[0][0]
    
    sql = "SELECT * FROM threads WHERE category_id='" + str(catId) + "'"
    result = db.session.execute(sql)
    
    return result.fetchall()

def get_byId(thId):
    sql = "SELECT * FROM threads WHERE id='" + thId + "'"
    result = db.session.execute(sql)
    return result.fetchall()

def add_new(catId, uId, content):
    sql = "INSERT INTO threads (category_id, user_id, content) VALUES (:catId, :uId, :content)"
    db.session.execute(sql, {"catId":catId, "uId":uId, "content":content})
    db.session.commit()
    return True