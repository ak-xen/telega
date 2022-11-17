from aiogram.filters import BaseFilter
from aiogram.types.message import Message
from data.sql_connection_personals_id import all_id_personals


class IsTrueUsers(BaseFilter):
    async def __call__(self, msg: Message):
        users = await all_id_personals()
        users = [i[0] for i in users]
        user = str(msg.from_user.id)
        if user not in users:
            await msg.answer('Только для зарегистрированных пользователей!')
            return False
        return True
