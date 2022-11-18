from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardBuilder

def button_start():
    btn_start = KeyboardButton(text=r'/ключи')
    btn_stop = KeyboardButton(text=r'/стоп')
    builder = ReplyKeyboardBuilder()

    builder.add(btn_start, btn_stop)
    return builder.as_markup(resize_keyboard=True)