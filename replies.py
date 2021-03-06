from db import db

def get_all():
    sql = "SELECT id, content, thread_id, user_id, sent_at FROM replies"
    result = db.session.execute(sql)
    return result.fetchall()

def get_byThread(thId):
    sql = "SELECT users.username, replies.content, replies.sent_at FROM replies " + \
        "INNER JOIN users ON users.id = replies.user_id WHERE thread_id=:thId " + \
        "ORDER BY replies.sent_at ASC"
    result = db.session.execute(sql, {"thId": thId})
    return result.fetchall()


def add_new(content, thId, uId):
    sql = "INSERT INTO replies (content, thread_id, user_id, sent_at) VALUES (:content, :thId, :uId, NOW())"
    db.session.execute(sql, {"content": content, "thId": thId, "uId": uId})
    db.session.commit()
    return True

def search(searchterm):
    sql = "SELECT id, content, thread_id, user_id, sent_at, COUNT(*) " + \
    "FROM replies WHERE content LIKE :searchterm GROUP BY id"
    result = db.session.execute(sql, {"searchterm": searchterm})
    return result.fetchall()