import re
import sqlite3


def connect_to_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    return conn, cursor


def set_user(user_id, message):
    password = re.search(r'\S+$', message).group(0)
    user = [(user_id, password, 0, 0)]
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", user)
    conn.commit()


def id_exists(user_id):
    conn, cursor = connect_to_db()
    r = """SELECT * FROM users WHERE id = '%s'""" % user_id
    sql = cursor.execute(r)
    response = sql.fetchall()
    if len(response) > 0:
        return True
    else:
        return False
