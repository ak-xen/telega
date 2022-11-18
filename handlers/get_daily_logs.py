from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from filters.id_filter import IsTrueUsers
from data.create_daily_log import draw_daily_table
import asyncio
from support import remove_file

get_daily = Router()


@get_daily.message(IsTrueUsers(), Command(commands=['daily']))
async def add_key(message: types.Message, command: CommandObject):
    if command.args:
        try:
            date = command.args
            path = f'data/daily_logs/temp/{date}.html'
            await draw_daily_table(date)
            await message.answer("<b>Ожидайте, документ скоро загрузится...</b>")
            html_table = types.FSInputFile(path)
            await asyncio.sleep(1)
            await message.answer_document(html_table)
            await asyncio.sleep(3)
            await message.answer('<b>Документ готов. Откройте его в любом из браузеров вашего устройства!</b>')
            await remove_file(path)
        except (ValueError, FileNotFoundError):
            await message.answer('<b>Не правильный формата даты! Или в этот день не было запросов ключей!</b>')
    else:
        await message.answer('<b>Введите после команды /daily запрашиваемую дату!</b>')

