import os


def on_startup():
    print("Bot was started!")


async def remove_file(path):
    os.remove(path)
