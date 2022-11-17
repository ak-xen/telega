from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from data.sql_connection_keys import get_key_status
from keyboards import kb_get_key, kb_start
from filters.id_filter import IsTrueUsers

start_router = Router()


class GetAddr(StatesGroup):
    getting_adres = State()


@start_router.message(IsTrueUsers(), Command(commands=['старт']))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("<b>Включен режим запроса адресов!</b>", reply_markup=kb_start.button_start())
    await state.set_state(GetAddr.getting_adres)


@start_router.message(IsTrueUsers(), GetAddr.getting_adres)
async def print_addr(message: types.Message, state: FSMContext):
    if message.text == '/стоп':
        await state.clear()
        await message.answer('<b>Режим запроса адресов выключен!</b>')
        return

    try:
        adres = ''.join(message.text.lower().split())
        key, addr, description, acces, time, date = await get_key_status(adres)
        if acces != "False":
            await message.answer(
                f'Адрес: {addr}\nКлюч № {key}\nДоступ: {description}\nКлюч у: {acces} Время: {time} Дата: {date}')
        else:
            await message.answer(f'Адрес: {addr}\nКлюч № {key}\nДоступ: {description}\nУ кого ключ: {acces}',
                                 reply_markup=kb_get_key.get_key_kb(key).as_markup())
    except:
        await message.answer('<b>Не корректно введен адрес или команда!</b>')

    await state.set_state(GetAddr.getting_adres)
