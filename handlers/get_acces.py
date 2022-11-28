from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from data.sql_connection_keys import get_key_status
from keyboards import access_kb, started_kb
from filters.id_filter import IsTrueUsers

access_route = Router()


class GetAccess(StatesGroup):
    accessed = State()


@access_route.message(IsTrueUsers(), Command(commands=['доступ']))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("<b>Включен режим 'Доступ'!</b>", reply_markup=access_kb.access_btn())
    await state.set_state(GetAccess.accessed)


@access_route.message(IsTrueUsers(), GetAccess.accessed)
async def print_addr(message: types.Message, state: FSMContext):
    if message.text == '/стоп':
        await state.clear()
        await message.answer('<b>Режим "Доступ" выключен!</b>', reply_markup=started_kb.btns_start())
        return

    try:
        address = ''.join(message.text.lower().split())
        address = address.replace('ё', "е")
        key, addr, description, acces, time, date = await get_key_status(address)
        await message.answer(
            f'Адрес: {addr}\nДоступ: {description}\nКлюч у: {acces} Время: {time} Дата: {date}')
    except:
        await message.answer('<b>Не корректно введен адрес или команда!</b>')

    await state.set_state(GetAccess.accessed)
