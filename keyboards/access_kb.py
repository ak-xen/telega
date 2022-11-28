from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder


def access_btn():
    btn_stop = KeyboardButton(text=r'/стоп')
    builder = ReplyKeyboardBuilder()

    builder.add(btn_stop)
    return builder.as_markup(resize_keyboard=True)
