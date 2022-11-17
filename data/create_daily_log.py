import pandas as pd
import pretty_html_table
import os


async def get_daily_file_names():
    names = os.listdir('data/daily_logs')
    return names


async def create_new_xlsx(name):
    with open(f'data/daily_logs/{name}.xlsx', 'w') as file:
        file.close()


async def find_name_xlsx(date):
    names = await get_daily_file_names()
    find_date = f'{date}.xlsx'
    if find_date not in names:
        await create_new_xlsx(date)
        return True, f'data/daily_logs/{date}.xlsx'
    return False, f'data/daily_logs/{date}.xlsx'


async def add_date_in_xlsx(key, addr, acces, time, date):
    df = pd.DataFrame({
        'KEY': [key],
        'ADDR': [addr],
        'ACCES': [acces],
        'TIME': [time],
        'DATE': [date]
    })
    flag, file_name = await find_name_xlsx(date)
    if flag:
        df.to_excel(file_name, index=False)
    else:
        df_read = pd.read_excel(file_name)
        df = pd.concat([df_read, df], ignore_index=True)
        df['ACCES'] = sorted(df['ACCES'])
        df.to_excel(file_name, index=False)


async def draw_daily_table(table_name):
    df = pd.read_excel(f'data/daily_logs/{table_name}.xlsx')
    html_table = pretty_html_table.build_table(df, 'green_light', text_align='center',
                                               width='auto')

    html_head = '''<!doctype html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>'''

    html_write = html_head + '\n' + html_table
    with open(f'data/daily_logs/temp/{table_name}.html', 'w', encoding='utf-8') as file:
        file.write(html_write)
