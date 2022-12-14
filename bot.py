import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from support import on_startup
from handlers import put_key, add_new_key, get_key_log, help_hand,start
from handlers import add_new_id, del_id, view_all_id, one_person_stats, get_daily_logs
from handlers import edit_desc, create_config, get_acces, keys_get, backup_db


async def main():
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(start.starts)
    dp.include_router(put_key.put)
    dp.include_router(add_new_key.add)
    dp.include_router(add_new_id.add_id)
    dp.include_router(del_id.del_id)
    dp.include_router(view_all_id.view_id)
    dp.include_router(one_person_stats.person)
    dp.include_router(get_daily_logs.get_daily)
    dp.include_router(get_key_log.get_log)
    dp.include_router(help_hand.help_router)
    dp.include_router(edit_desc.edit)
    dp.include_router(create_config.make_config)
    dp.include_router(get_acces.access_route)
    dp.include_router(keys_get.keys)
    dp.include_router(backup_db.backup)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=on_startup())


if __name__ == '__main__':
    asyncio.run(main())
