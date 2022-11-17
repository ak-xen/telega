from aiogram import Router, types
from data.sql_connection_keys import set_status
from filters.id_filter import IsTrueUsers
get_callback = Router()


@get_callback.callback_query(IsTrueUsers(), text_startswith='key_get_')
async def getting_key(callback: types.CallbackQuery):
    value = callback.data.strip('key_get_')
    if value.isdigit():
        if await(set_status(value, str(callback.from_user.id))):
            await callback.message.answer(text=f'<u>Ключ №{value} взят !</u>')
    else:
        await callback.message.answer(text='<b>Ключа не существует!</b>')
    await callback.answer()
