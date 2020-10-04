from db import db

def send(sender, recipient, content):
    sql = "INSERT INTO privateMessages (sender, recipient, content, sent_at) values (:sender, :recipient, :content, NOW())"
    db.session.execute(sql, {"sender":sender, "recipient":recipient, "content":content})
    db.session.commit()
    return

def get_sentToMe(my_id):
    sql = "SELECT users.username, privateMessages.content, privateMessages.sent_at FROM privateMessages, users " + \
        "WHERE recipient=:my_id AND users.id=privateMessages.sender"
    result = db.session.execute(sql, {"my_id":my_id})
    return result.fetchall()

def get_sentByMe(my_id, recipientId):
    sql = "SELECT privateMessages.content, privateMessages.sent_at FROM privateMessages WHERE recipient=:recipientId " + \
        "AND sender=:my_id ORDER BY privateMessages.sent_at ASC"
    result = db.session.execute(sql, {"recipientId":recipientId, "my_id":my_id})
    return result.fetchall()