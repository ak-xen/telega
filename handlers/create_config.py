import asyncio
import support

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from data.config_data.config_creator import transliteration
from keyboards import commutator_kb
from filters.id_filter import IsTrueUsers
from data.config_data import config_creator

make_config = Router()

conf_dict = {}


class MakeConfig(StatesGroup):
    choice_commutator = State()
    ip = State()
    netmask = State()
    vlan = State()
    gateway = State()
    addr_station = State()
    end = State()


@make_config.message(IsTrueUsers(), Command(commands=['conf']))
async def cmd_start(message: types.Message, state: FSMContext):
    if message.text == '/стоп':
        await state.clear()
        await message.answer('<b>Режим запроса адресов выключен!</b>')
        return
    await message.answer("<b>Выберите модель комутатора!</b>", reply_markup=commutator_kb.get_conf().as_markup())
    await state.set_state(MakeConfig.ip)


@make_config.callback_query(IsTrueUsers(), MakeConfig.ip)
async def print_addr(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == '/стоп':
        await state.clear()
        await callback.answer('<b>Режим запроса адресов выключен!</b>')
        return
    conf_dict['commutator'] = callback.data
    await callback.message.answer("<b>Введите IP-адрес!</b>")
    await callback.answer()
    await state.set_state(MakeConfig.netmask)


@make_config.message(IsTrueUsers(), MakeConfig.netmask)
async def print_addr(message: types.Message, state: FSMContext):
    if message.text == '/стоп':
        await state.clear()
        await message.answer('<b>Режим запроса адресов выключен!</b>')
        return
    conf_dict['ip'] = message.text
    await message.answer("<b>Введите маску сети!</b>")
    await state.set_state(MakeConfig.vlan)


@make_config.message(IsTrueUsers(), MakeConfig.vlan)
async def print_addr(message: types.Message, state: FSMContext):
    if message.text == '/стоп':
        await state.clear()
        await message.answer('<b>Режим запроса адресов выключен!</b>')
        return
    conf_dict['netmask'] = message.text
    await message.answer("<b>Введите VLAN управления!</b>")
    await state.set_state(MakeConfig.gateway)


@make_config.message(IsTrueUsers(), MakeConfig.gateway)
async def print_addr(message: types.Message, state: FSMContext):
    if message.text == '/стоп':
        await state.clear()
        await message.answer('<b>Режим запроса адресов выключен!</b>')
        return
    conf_dict['vlan'] = message.text
    await message.answer("<b>Введите Шлюз!</b>")
    await state.set_state(MakeConfig.addr_station)


@make_config.message(IsTrueUsers(), MakeConfig.addr_station)
async def print_addr(message: types.Message, state: FSMContext):
    if message.text == '/стоп':
        await state.clear()
        await message.answer('<b>Режим запроса адресов выключен!</b>')
        return
    conf_dict['gateway'] = message.text
    await message.answer("<b>Введите Адрес установки!</b>")
    await state.set_state(MakeConfig.end)


@make_config.message(IsTrueUsers(), MakeConfig.end)
async def print_addr(message: types.Message, state: FSMContext):
    if message.text == '/стоп':
        await state.clear()
        await message.answer('<b>Режим запроса адресов выключен!</b>')
        return
    addr = await transliteration(message.text)
    conf_dict['addr_station'] = addr
    await message.answer('<b>Ожидайте, идет конфигурация!</b>')
    await asyncio.sleep(1)
    text = await config_creator.output_config(conf_dict)
    await message.answer(text)
    path_to_file = await config_creator.config_file(conf_dict['addr_station'], conf_dict['commutator'], conf_dict['ip'],
                                                    text)
    file = types.FSInputFile(path_to_file)
    await message.answer_document(file)
    await asyncio.sleep(3)
    await support.remove_file(path_to_file)
    await state.clear()

