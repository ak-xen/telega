from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_key_kb(key_number):
    builder = InlineKeyboardBuilder()
    button_get = InlineKeyboardButton(text=f'Взять ключ № {key_number}', callback_data=f'key_get_{key_number}')
    builder.add(button_get)
    return builder
