from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from data import sql_connection_keys
from filters.id_filter import IsTrueUsers

edit = Router()


@edit.message(IsTrueUsers(), Command(commands=['edit']))
async def put_key(message: types.Message, command: CommandObject):
    if command.args:
        addr, *new_description = command.args.split(',')
        get_addr = ''.join(addr.lower().split())
        new_description = ', '.join(new_description)
        if new_description:
            await message.answer('Ожидайте....')
            await sql_connection_keys.edit_description(get_addr, new_description.lstrip())
            await message.answer(f'Доступ для адреса {addr} обновлен!')
            key, addr, description, acces, *_ = await sql_connection_keys.get_key_status(get_addr)
            await message.answer(
                f'\n\nАдрес: {addr}\nКлюч №: {key}\nДоступ: {description}\n')
        else:
            await message.answer('<b>Укажите после адреса, через запятую доступ!</b>')

    else:
        await message.answer('<b>После команды /edit укажите адрес и новый доступ через запятую!</b>')
