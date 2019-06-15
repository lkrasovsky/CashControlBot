from telebot import types


def login_or_register():
    login_or_register_keyboard = types.ReplyKeyboardMarkup()
    login_or_register_keyboard.row("Регистрация", "Вход")

    return login_or_register_keyboard


def main_menu():
    main_menu_keyboard = types.ReplyKeyboardMarkup()
    main_menu_keyboard.row("/start")
    main_menu_keyboard.row("Новая операция", "Баланс 💰")
    main_menu_keyboard.row("Операции 📄")
    main_menu_keyboard.row("О боте 🤖", "Разработчик 👼")

    return main_menu_keyboard


def cash_or_card():
    cash_or_card_keyboard = types.ReplyKeyboardMarkup()
    cash_or_card_keyboard.row("Наличные", "Карта")
    return cash_or_card_keyboard


def operations():
    operations_keyboard = types.ReplyKeyboardMarkup()
    operations_keyboard.row("Пополнить 💵", "Пополнить 💳")
    operations_keyboard.row("Списать 💵", "Списать 💳")
    operations_keyboard.row("Изменить 💵", "Изменить 💳")

    return operations_keyboard