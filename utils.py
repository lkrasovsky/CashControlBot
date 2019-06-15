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


def get_password(user_id):
    conn, cursor = connect_to_db()
    r = """SELECT password FROM users WHERE id = '%s'""" % user_id
    sql = cursor.execute(r)
    response = sql.fetchall()
    if len(response) > 0:
        return response[0][0]
    else:
        return None


def get_money(user_id):
    conn, cursor = connect_to_db()
    r = """SELECT cash, card FROM users WHERE id = '%s'""" % user_id
    sql = cursor.execute(r)
    response = sql.fetchall()
    cash = float(response[0][0])
    card = float(response[0][1])
    return cash, card


def add_cash(user_id, sum):
    cash, card = get_money(user_id)
    result = float(cash + sum)

    conn, cursor = connect_to_db()
    cursor.executescript("""UPDATE users SET cash='%s' WHERE id='%s'""" % (result, user_id))
    return "Успешно!"


def subtract_cash(user_id, sum):
    cash, card = get_money(user_id)
    if cash >= sum:
        result = float(cash - sum)

        conn, cursor = connect_to_db()
        cursor.executescript("""UPDATE users SET cash='%s' WHERE id='%s'""" % (result, user_id))

        return "Успешно!"
    else:
        return "Не достаточно средств."


def edit_cash(user_id, sum):
    pass


def add_card(user_id, sum):
    cash, card = get_money(user_id)
    result = float(card + sum)

    conn, cursor = connect_to_db()
    cursor.executescript("""UPDATE users SET card='%s' WHERE id='%s'""" % (result, user_id))
    return "Успешно!"


def subtract_card(user_id, sum):
    cash, card = get_money(user_id)
    if card >= sum:
        result = float(card - sum)

        conn, cursor = connect_to_db()
        cursor.executescript("""UPDATE users SET card='%s' WHERE id='%s'""" % (result, user_id))

        return "Успешно!"
    else:
        return "Не достаточно средств."


def edit_card(user_id, sum):
    pass
