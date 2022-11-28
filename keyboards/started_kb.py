from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder

def btns_start():
    btn_start = KeyboardButton(text=r'/ключи')
    btn_stop = KeyboardButton(text=r'/доступ')
    builder = ReplyKeyboardBuilder()

    builder.add(btn_start, btn_stop)
    return builder.as_markup(resize_keyboard=True)