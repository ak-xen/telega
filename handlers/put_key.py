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
        uid = str(message.from_user.id)
        all_keys = await sql_connection_keys.get_all_keys()
        all_keys = list(map(lambda x: str(x[0]), all_keys))
        for k in key:
            if k.strip() in all_keys and await sql_connection_keys.get_access(k, uid):
                keys.append(k)
        if keys:
            await sql_connection_keys.del_status(keys, uid)
            keys = ','.join(keys)
            await message.answer(f'<u>Ключ №{keys} положен на место!</u>')
        else:
            await message.answer('<u>Нет ключей, которые можно положить!</u>')
    else:
        await message.answer('<b>Укажите номер ключа, который хотите положить после команды /сдать !</b>')
