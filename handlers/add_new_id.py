from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from data.sql_connection_personals_id import add_new_id
from filters.id_filter import IsTrueUsers


add_id = Router()


@add_id.message(IsTrueUsers(), Command(commands=['add_id']))
async def id_add(message: types.Message, command: CommandObject):
    if command.args:
        try:
            id, name = command.args.split(',')
            await add_new_id(id.strip(), name.strip())
            await message.answer(f'<u>В базу был добавлен!\nID: {id}\nName: {name}</u>')
        except ValueError:
            await message.answer('<b>Id и имя нужно обязательно ввести через запятую</b>')
    else:
        await message.answer('<b>Введите после команды /add_id id, имя!</b>')
