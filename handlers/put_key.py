from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from data import sql_connection_keys
from filters.id_filter import IsTrueUsers

put = Router()


@put.message(IsTrueUsers(), Command(commands=['сдать']))
async def put_key(message: types.Message, command: CommandObject):
    if command.args:
        key = command.args.split(',')
        keys = []
        for k in key:
            if await sql_connection_keys.get_access(k):
                keys.append(k)
        if keys:
            await sql_connection_keys.del_status(keys, str(message.from_user.id))
            keys = ','.join(keys)
            await message.answer(f'<u>Ключ №{keys} положен на место!</u>')
        else:
            await message.answer('<u>Нет ключей, которые можно положить!</u>')
    else:
        await message.answer('<b>Укажите номер ключа, который хотите положить после команды /put !</b>')
