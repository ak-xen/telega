from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from data.sql_connection_keys import id_find
from filters.id_filter import IsTrueUsers


person = Router()


@person.message(IsTrueUsers(), Command(commands=['person']))
async def id_add(message: types.Message, command: CommandObject):
    if command.args:
        id = command.args
        result_text = ''
        name, res = await id_find(id.strip())
        if res:
            for key, addr, time, date in res:
                result_text += f'<u>Ключ №: {key} Адрес: {addr} Время: {time} Дата: {date}\n</u>'
            await message.answer(f'<u>Ключи на {name}!\n{result_text}</u>')
        else:
            await message.answer(f'<b>У пользователя {name} нет ключей!</b>')
    else:
        await message.answer('<b>Введите после команды /person id!</b>')
