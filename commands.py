from aiogram import types
from create_bot import bot
from model import *
from chat import setPlayer, getPlayer


async def start(message: types.Message):
    player = message.from_user
    setPlayer(player)
    await bot.send_message(player.id, f'Здравствуй, {player.first_name}!')
    await bot.send_message(player.id, f'Напиши /game чтобы начать.')
    
    # print(message.text)
    # print(message.from_user.first_name)

# async def player_turn(message: types.Message):
#     countBons=message

async def game(message: types.Message):
    pass


async def stop(message: types.Message):
    print(message.text)
    print(message.from_user.first_name)
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, game over!')

async def anything(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.text} -- what is it?')
    