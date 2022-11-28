from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from filters.id_filter import IsTrueUsers

backup = Router()


@backup.message(IsTrueUsers(), Command(commands=['backup']))
async def get_backup(message: types.Message):
    path = 'data/data.db'
    file = types.FSInputFile(path)
    await message.answer('Ожидайте идет подготовка документа...')
    await message.answer_document(file)
