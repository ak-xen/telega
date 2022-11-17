# Файл для связи с таблицей keys
import asyncio
import aiosqlite
import time
from data import create_daily_log


async def get_key_status(addres: str):
    '''
    Функция будет получать на вход адрес и
    возвращать номер ,и статус ключа с коментариями.
    :param addres: Строка адреса, предварительно обработанная (если идут слова то делаем заглавные буквы)
    :return:
    '''

    async with aiosqlite.connect('data/data.db') as db:
        async with db.execute(f"SELECT key, addr,  description, acces, time, date FROM keys "
                              f"WHERE get_addr='{addres}';") as cursor:
            key_status = await cursor.fetchone()
            key, addr, description, acces, time, date = key_status
        if acces != 'False':
            async with db.execute(f'SELECT name FROM personals_id WHERE id={acces}') as cursor:
                name = await cursor.fetchone()
                name = name[0]
                return key, addr, description, name, time, date
        return key, addr, description, acces, time, date


async def get_log_path(db, key, name, id):
    async with db.execute(f'SELECT addr_log FROM keys WHERE key="{key}"') as cursor:
        path = await cursor.fetchone()
        path = path[0]
        if not path:
            if key.isdigit():
                path = f"data/logs/{key}_log.txt"
            await db.execute(f"UPDATE keys SET addr_log='{path}' WHERE key='{key}'")
            with open(path, 'w', encoding='utf-8') as file:
                file.write(f'Ключ взял: {name} : {id} Время: {time.strftime("%H:%M %d.%m.%Y")}\n')
            await db.commit()
        else:
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'Ключ взял: {name} : {id} Время: {time.strftime("%H:%M %d.%m.%Y")}\n')


async def set_status(key: str, id: str):
    async with aiosqlite.connect('data/data.db') as db:
        async with db.execute(f'SELECT name FROM personals_id WHERE id="{id}"') as cursor:
            name = await cursor.fetchone()
            name = name[0]
        async with db.execute(f'SELECT addr FROM keys WHERE key="{key}"') as cur:
            addr = await cur.fetchone()
            addr = addr[0]

        await db.execute(
            f"UPDATE keys SET acces='{id}', time='{time.strftime('%H:%M')}', date='{time.strftime('%d.%m.%Y')}' WHERE key='{key}'")
        await db.commit()
        await get_log_path(db, key, name, id)
        await create_daily_log.add_date_in_xlsx(key, addr, f'{id}/{name}', time.strftime('%H:%M'),
                                                time.strftime('%d.%m.%Y'))
    return True


async def del_status(key, id):
    async with aiosqlite.connect('data/data.db') as db:
        for item in key:
            async with db.execute(f'SELECT name FROM personals_id WHERE id="{id}"') as cursor:
                name = await cursor.fetchone()
                name = name[0]
            await db.execute(f"UPDATE keys SET acces='False', time='', date='' WHERE key='{item.strip()}'")
            await db.commit()
            async with db.execute(f"SELECT addr_log FROM keys WHERE key='{item.strip()}'") as cursor:
                path = await cursor.fetchone()
                path = path[0]
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'Положил ключ: {name} Время: {time.strftime("%H:%M %d.%m.%Y")}\n')
            await asyncio.sleep(1)


async def add_new_key(key, addr, description):
    k = key
    get_addr = ''.join(addr.lower().split())
    async with aiosqlite.connect('data/data.db') as db:
        await db.execute(
            f'INSERT INTO keys (key, get_addr, addr, description, acces) VALUES ("{k}", "{get_addr}", "{addr}", "{description}", "False")')
        await db.commit()


async def id_find(id):
    async with aiosqlite.connect('data/data.db') as db:
        async with db.execute(f"SELECT name FROM personals_id WHERE id='{id}'") as cursor:
            names = await cursor.fetchone()
            names = names[0]
        async with db.execute(f"SELECT key, addr, time, date FROM keys WHERE acces='{id}'") as cursor:
            result = await cursor.fetchall()
            return names, result


async def put_all_keys(id):
    async with aiosqlite.connect('data/data.db') as db:
        async with db.execute(f'SELECT key FROM keys WHERE acces="{id}"') as cursor:
            keys = await cursor.fetchall()
            keys = [str(i[0]) for i in keys]
            await del_status(keys, id)
            return keys


async def edit_description(get_addr, new_description):
    async with aiosqlite.connect('data/data.db') as db:
        await db.execute(f"UPDATE keys SET description='{new_description}' WHERE get_addr='{get_addr}'")
        await db.commit()