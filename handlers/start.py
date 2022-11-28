from aiogram import Router, types
from aiogram.filters import Command
from keyboards import started_kb
from filters.id_filter import IsTrueUsers

starts = Router()


@starts.message(IsTrueUsers(), Command(commands=['start']))
async def started(message: types.Message):
    await message.answer("<b>Бот включен!</b>", reply_markup=started_kb.btns_start())




