import re
import sqlite3

import telebot

import bot_info  # file keeping a bot token

bot = telebot.TeleBot(bot_info.token)
types = telebot.types

# creating SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
try:
    cursor.execute("""CREATE TABLE users
                      (id text, password text, cash integer, card integer)
                   """)
except sqlite3.OperationalError:
    pass
conn.commit()


def create_enter_keyboard():
    enter_keyboard = types.ReplyKeyboardMarkup()
    enter_keyboard.row("Регистрация", "Вход")

    return enter_keyboard


def create_menu_keyboard():
    menu_keyboard = types.ReplyKeyboardMarkup()
    menu_keyboard.row("/start")
    menu_keyboard.row("Пополнить 🔼", "Списать 🔽")
    menu_keyboard.row("Баланс 💰")
    menu_keyboard.row("Операции 📄")
    menu_keyboard.row("О боте 🤖", "Разработчик 👼")

    return menu_keyboard


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id: str = str(message.from_user.id)
    bot.send_message(user_id,
                     "Привет. Для того, чтобы использовать бота, необходимо загерестрироваться или войти в систему.",
                     reply_markup=create_enter_keyboard())


@bot.message_handler(content_types=['text'])
def message_handler(message):
    user_id: str = str(message.from_user.id)

    if message.text == "Регистрация":
        bot.send_message(user_id,
                         "Ваш id - " + user_id + ". " + "Для того, чтобы установить пароль, введите: \n\n" + "pass - *ваш новый пароль*")

    elif message.text == "Вход":
        bot.send_message(user_id, "Введите ваш никнейм.")

    elif "pass" in message.text:
        password = re.search(r'\S+$', message.text).group(0)
        user = [(user_id, password, 0, 0)]
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", user)
        conn.commit()

        bot.send_message(user_id, "Регистрация завершена успешно.")


bot.polling(none_stop=True, interval=0)
