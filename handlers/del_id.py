from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from data.sql_connection_personals_id import delete_id
from filters.id_filter import IsTrueUsers


del_id = Router()


@del_id.message(IsTrueUsers(), Command(commands=['del_id']))
async def id_del(message: types.Message, command: CommandObject):
    if command.args:
        id = command.args
        await delete_id(id.strip())
        await message.answer(f'<u>ID: {id} быд удален из базы!</u>')
    else:
        await message.answer('<b>Введите после команды /del_id id!</b>')
