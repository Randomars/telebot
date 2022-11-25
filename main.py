from aiogram import executor
from create_bot import *
import handlers


async def onStart(_):
    print('Bot ready to work.')

handlers.registred_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=onStart)