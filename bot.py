import re

import telebot

import bot_info  # file keeping a bot token
import keyboards
import utils

bot = telebot.TeleBot(bot_info.token)
types = telebot.types


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id: str = str(message.from_user.id)
    bot.send_message(user_id,
                     "Привет. Для того, чтобы использовать бота, необходимо загерестрироваться или войти в систему.",
                     reply_markup=keyboards.login_or_register())


@bot.message_handler(content_types=['text'])
def message_handler(message):
    user_id: str = str(message.from_user.id)

    if message.text == "Регистрация":
        if not utils.id_exists(user_id):
            bot.send_message(user_id,
                             "Ваш id - " + user_id + ". " + "Для того, чтобы установить пароль, введите:" +
                             "\n\nnew - *ваш новый пароль*")
        else:
            bot.send_message(user_id, "Пользователь с id " + user_id + " уже существует. ",
                             reply_markup=keyboards.login_or_register())

    elif message.text == "Вход":
        if utils.id_exists(user_id):
            bot.send_message(user_id, "Ваш id: " + user_id + ". " + "\n\nВведите пароль (pass - *ваш пароль*):")
        else:
            bot.send_message(user_id, "Вы ещё не зарегестрированы.", reply_markup=keyboards.login_or_register())

    elif "new" in message.text:
        utils.set_user(user_id, message.text)
        bot.send_message(user_id, "Регистрация завершена успешно.")

    elif "pass" in message.text:
        password = re.search(r'\S+$', message.text).group(0)
        if password == utils.get_password(user_id):
            bot.send_message(user_id, "Вы вошли в систему.")
        else:
            bot.send_message(user_id, "Неверный пароль. Повторите попытку.")


bot.polling(none_stop=True, interval=0)
