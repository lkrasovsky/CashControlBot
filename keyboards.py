from telebot import types


def enter():
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
