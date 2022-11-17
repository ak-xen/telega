from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_conf():
    builder = InlineKeyboardBuilder()
    button_1 = InlineKeyboardButton(text='Fiberhome S48020-10T-GF', callback_data=f'Fiberhome S48020-10T-GF')
    button_2 = InlineKeyboardButton(text='Fiberhome S48020-28T-GF', callback_data=f'Fiberhome S48020-28T-GF')
    button_3 = InlineKeyboardButton(text='Fiberhome S48020-52T-GF', callback_data=f'Fiberhome S48020-52T-GF')
    button_4 = InlineKeyboardButton(text='D-link DES-3200-26', callback_data=f'D-link DES-3200-26')
    button_5 = InlineKeyboardButton(text='D-link DES-3200-26/C1', callback_data=f'D-link DES-3200-26/C1')
    button_6 = InlineKeyboardButton(text='D-link DES-3200-28/C1A', callback_data=f'D-link DES-3200-28/C1A')
    button_7 = InlineKeyboardButton(text='D-link DES-3200-52/C1', callback_data=f'D-link DES-3200-52/C1')
    builder.add(button_1)
    builder.add(button_2)
    builder.add(button_3)
    builder.add(button_4)
    builder.add(button_5)
    builder.add(button_6)
    builder.add(button_7)
    builder.adjust(1)
    return builder

