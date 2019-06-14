from telebot import types


def login_or_register():
    login_or_register_keyboard = types.ReplyKeyboardMarkup()
    login_or_register_keyboard.row("Регистрация", "Вход")

    return login_or_register_keyboard


def main_menu():
    main_menu_keyboard = types.ReplyKeyboardMarkup()
    main_menu_keyboard.row("/start")
    main_menu_keyboard.row("Пополнить 🔼", "Списать 🔽")
    main_menu_keyboard.row("Баланс 💰")
    main_menu_keyboard.row("Операции 📄")
    main_menu_keyboard.row("О боте 🤖", "Разработчик 👼")

    return main_menu_keyboard
