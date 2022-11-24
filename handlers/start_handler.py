from aiogram import types
from bot import dp


@dp.message_handler(state="*", commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Hello, send photo to get its description and hashtags")
