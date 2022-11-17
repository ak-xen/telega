from aiogram import Router, types
from aiogram.filters import Command
from data.sql_connection_personals_id import view_all_id
from filters.id_filter import IsTrueUsers

view_id = Router()


@view_id.message(IsTrueUsers(), Command(commands=['view_id']))
async def id_view(message: types.Message):
    result = await view_all_id()
    result = [' - '.join(string) for string in result]
    result = '\n'.join(result)
    await message.answer(f'<b>Список всех юзеров!\n{result}</b>')


