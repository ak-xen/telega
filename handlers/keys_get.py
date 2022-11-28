from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from data.sql_connection_keys import set_status, get_key_status
from keyboards import kb_start
from filters.id_filter import IsTrueUsers

keys = Router()


class GetAddr(StatesGroup):
    get_keys = State()


@keys.message(IsTrueUsers(), Command(commands=['ключи']))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("<b>Включен режим  'Ключи'!</b>", reply_markup=kb_start.button_start())
    await state.set_state(GetAddr.get_keys)


@keys.message(IsTrueUsers(), GetAddr.get_keys)
async def print_addr(message: types.Message, state: FSMContext):
    if message.text == '/стоп':
        await state.clear()
        await message.answer('<b>Режим "Ключи" выключен!</b>')
        return

    try:
        addr = ''.join(message.text.lower().split())
        addr = addr.replace('ё', "е")
        key, addr, description, acces, time, date = await get_key_status(addr)
        if acces == 'False' and await(set_status(key, str(message.from_user.id).strip())):
            await message.answer(text=f'<u>Ключ №{key} взят !</u>')
        else:
            await message.answer(f'Ключ №{key} у {acces}\nВремя: {time} Дата: {date}')

    except:
        await message.answer('<b>Не корректно введен адрес или команда!</b>')

    await state.set_state(GetAddr.get_keys)
