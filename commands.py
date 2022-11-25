from aiogram import types
from create_bot import bot


async def start(message: types.Message):
    print(message.text)
    print(message.from_user.first_name)

async def stop(message: types.Message):
    print(message.text)
    print(message.from_user.first_name)
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, game over!')

async def anything(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.text} -- what is it?')
    