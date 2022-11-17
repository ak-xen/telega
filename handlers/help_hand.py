from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from filters.id_filter import IsTrueUsers

help_router = Router()


@help_router.message(IsTrueUsers(), Command(commands=['help']))
async def cmd_start(message: types.Message, command: CommandObject):
    if command.args == 'a':
        await message.answer('Включить режим запроса адресов.[/старт]\n'
                             'Выключить режим запроса адресов.[/стоп]\n'
                             'Снять с себя все ключи.[/Сдать_все_ключи]\n'
                             'Снять с себя ключ.[/сдать ключ, ключ, ...]\n'
                             'Редактировать доступ.[/edit адрес, доступ]\n'
                             'Суточный отчет.[/daily дд.мм.гг]\n'
                             'Отчет по одному ключу!.[/key №]\n'
                             'Добавить пользователя в базу.[/add_id id]\n'
                             'Добавить новый адрес в базу.[/add ключ, адрес, описание]\n'
                             'Удалить пользователя из базы.[/del_id id]\n'
                             'Количество ключей на одном пользователе.[/person id]\n'
                             'По смотреть список всех пользователей.[/view_id]')

    else:
        await message.answer('Включить режим запроса адресов.[/старт]\n'
                             'Выключить режим запроса адресов.[/стоп]\n'
                             'Снять с себя все ключи.[/Сдать_все_ключи]\n'
                             'Снять с себя ключ.[/сдать ключ, ключ, ...]\n'
                             'Отчет по одному ключу!.[/key №]')


