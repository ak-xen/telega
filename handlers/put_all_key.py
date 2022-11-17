from aiogram import Router, types
from aiogram.filters import Command
from filters.id_filter import IsTrueUsers
from data.sql_connection_keys import put_all_keys


put_all = Router()


@put_all.message(IsTrueUsers(), Command(commands=['Сдать_все_ключи']))
async def put_all_k(message: types.Message):
    keys = await put_all_keys(str(message.from_user.id))
    if keys:
        await message.answer(f'<u>Ключ № {", ".join(keys)} положен на место!</u>')
    else:
        await message.answer(f'<u>У вас нет ключей!</u>')

