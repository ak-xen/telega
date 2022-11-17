from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from data import sql_connection_keys
from filters.id_filter import IsTrueUsers

put = Router()


@put.message(IsTrueUsers(), Command(commands=['сдать']))
async def put_key(message: types.Message, command: CommandObject):
    if command.args:
        key = command.args.split(',')
        await sql_connection_keys.del_status(key, str(message.from_user.id))
        key = ','.join(key)
        await message.answer(f'<u>Ключ №{key} положен на место!</u>')
    else:
        await message.answer('<b>Укажите номер ключа, который хотите положить после команды /put !</b>')
