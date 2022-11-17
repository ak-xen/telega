# Файл для связи с таблицей personals_id
import aiosqlite


async def all_id_personals():
    async with aiosqlite.connect('data/data.db') as db:
        async with db.execute('SELECT id FROM personals_id') as cursor:
            list_id = await cursor.fetchall()
            return list_id


async def add_new_id(id, name):
    async with aiosqlite.connect('data/data.db') as db:
        await db.execute(f'INSERT INTO personals_id (id, name) VALUES ("{id}", "{name}")')
        await db.commit()


async def delete_id(id):
    async with aiosqlite.connect('data/data.db') as db:
        await db.execute(f'DELETE FROM personals_id WHERE id="{id}"')
        await db.commit()


async def view_all_id():
    async with aiosqlite.connect('data/data.db') as db:
        async with db.execute('SELECT * FROM personals_id') as cursor:
            result = await cursor.fetchall()
            return result
