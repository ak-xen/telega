from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from filters.id_filter import IsTrueUsers


get_log = Router()


@get_log.message(IsTrueUsers(), Command(commands=['key']))
async def add_key(message: types.Message, command: CommandObject):
    if command.args:
        try:
            key = command.args.strip()
            with open(f'data/logs/{key}_log.txt', encoding='utf-8') as file:
                text = file.readlines()
                if len(text) >= 5:
                    msg = '\n'.join(text[:5])
                    await message.answer(f'<b>Информация по последним 5 записям:</b>\n{msg}')
                else:
                    msg = '\n'.join(text)
                    await message.answer(f'<b>Информация по последним  записям:</b>\n{msg}')
        except (ValueError, FileNotFoundError):
            await message.answer('<b>Не верно указан ключ! Или этот ключ, еще не брали!</b>')
    else:
        await message.answer("После команды /key введите номер ключа!")
