from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardBuilder

def button_start():
    btn_start = KeyboardButton(text=r'/старт')
    btn_stop = KeyboardButton(text=r'/стоп')
    btn_putK = KeyboardButton(text=r'/Сдать_все_ключи')
    builder = ReplyKeyboardBuilder()

    builder.add(btn_start, btn_stop)
    builder.add(btn_putK)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)