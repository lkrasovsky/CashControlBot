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

    def send_message(message, reply_markup=None):
        bot.send_message(user_id, message, reply_markup=reply_markup)

    if message.text == "Регистрация":
        if not utils.id_exists(user_id):
            send_message("Ваш id - " + user_id + ". " + "Для того, чтобы установить пароль, введите:" +
                         "\n\nnew - *ваш новый пароль*")
        else:
            send_message("Пользователь с id " + user_id + " уже существует. ",
                         reply_markup=keyboards.login_or_register())

    elif "new" in message.text:
        utils.set_user(user_id, message.text)
        send_message("Регистрация завершена успешно.")

    elif message.text == "Вход":
        if utils.id_exists(user_id):
            send_message("Ваш id: " + user_id + ". " + "\n\nВведите пароль (pass - *ваш пароль*):")
        else:
            send_message("Вы ещё не зарегестрированы.", reply_markup=keyboards.login_or_register())

    elif "pass" in message.text:
        password = re.search(r'\S+$', message.text).group(0)
        if password == utils.get_password(user_id):
            send_message("Вы вошли в систему.", reply_markup=keyboards.main_menu())
        else:
            send_message("Неверный пароль. Повторите попытку.")

    elif message.text == "Новая операция":
        bot.send_message(user_id, "Выберите операцию.", reply_markup=keyboards.operations())

    ############### FOR CASH ###############

    elif message.text == "Пополнить 💵":
        cash, card = utils.get_money(user_id)
        send_message("Текущий баланс: " +
                     "\nНаличные - " + str(cash) +
                     "\nКарта - " + str(card) +
                     "\n\nВведите сумму:"
                     "\n\n+$ *ваша сумма*")

    elif "+$" in message.text:
        sum = float(re.search(r'\S+$', message.text).group(0))
        result = utils.add_cash(user_id, sum)
        cash, card = utils.get_money(user_id)
        send_message(result +
                     "\n\nТекущий баланс: " +
                     "\nНаличные - " + str(cash) +
                     "\nКарта - " + str(card))

    elif message.text == "Списать 💵":
        cash, card = utils.get_money(user_id)
        send_message("\n\nТекущий баланс: " +
                     "\nНаличные - " + str(cash) +
                     "\nКарта - " + str(card) +
                     "\n\nВведите сумму:"
                     "\n\n-$ *ваша сумма*")

    elif "-$" in message.text:
        sum = float(re.search(r'\S+$', message.text).group(0))
        result = utils.subtract_cash(user_id, sum)
        cash, card = utils.get_money(user_id)
        send_message(result +
                     "\n\nТекущий баланс: " +
                     "\nНаличные - " + str(cash) +
                     "\nКарта - " + str(card))

    elif message.text == "Изменить 💵":
        pass

    ########################################

    ############### FOR CARD ###############
    elif message.text == "Пополнить 💳":
        send_message("Введите сумму:"
                     "\n\n++ *ваша сумма*")

    elif "++" in message.text:
        sum = float(re.search(r'\S+$', message.text).group(0))
        result = utils.add_card(user_id, sum)
        cash, card = utils.get_money(user_id)
        send_message(result +
                     "\n\nТекущий баланс: " +
                     "\nНаличные - " + str(cash) +
                     "\nКарта - " + str(card))

    elif message.text == "Списать 💳":
        send_message("Введите сумму:"
                     "\n\n-- *ваша сумма*")

    elif "--" in message.text:
        sum = float(re.search(r'\S+$', message.text).group(0))
        result = utils.subtract_card(user_id, sum)
        cash, card = utils.get_money(user_id)
        send_message(result +
                     "\n\nТекущий баланс: " +
                     "\nНаличные - " + str(cash) +
                     "\nКарта - " + str(card))

    elif message.text == "Изменить 💳":
        pass

    ########################################

    elif message.text == "Баланс 💰":
        cash, card = utils.get_money(user_id)
        send_message("Наличные: " + str(cash) + "." +
                     "\nКарта: " + str(card) + ".")

    elif message.text == "О боте 🤖":
        send_message("Раздел находится на стадии разработки.")
        # TODO info, how to use bot

    elif message.text == "Разработчик 👼":
        send_message("Лев Красовский" +
                     "\n@lkrasovsky" +
                     "\n\nМинск, Беларусь")


bot.polling(none_stop=True, interval=0)
