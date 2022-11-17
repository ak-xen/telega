from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from data.sql_connection_keys import add_new_key
from filters.id_filter import IsTrueUsers


add = Router()


@add.message(IsTrueUsers(), Command(commands=['add']))
async def add_key(message: types.Message, command: CommandObject):
    if command.args:
        try:
            key, addr, *description = command.args.split(',')
            description = ",".join(map(str.strip, description))
            await add_new_key(key, addr.strip(), description)
            await message.answer(
                f'<u>В базу было добавлено!\nКлюч № {key}\nАдрес: {addr.strip()}\nОписание: {description}</u>')
        except ValueError:
            await message.answer('<b>Ключ, адрес и описание нужно вводить через запятую!</b>')
    else:
        await message.answer('<b>Введите после команды /add номер ключа, адрес, описание!</b>')
