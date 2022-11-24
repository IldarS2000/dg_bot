from aiogram import types
from bot import dp


@dp.message_handler(state='*', commands='help')
async def cmd_help(message: types.Message):
    await message.answer("send photo to get its description and hashtags")
