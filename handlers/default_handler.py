from aiogram import types
from bot import dp


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def cmd_default_handler(message: types.Message):
    await message.answer("unknown command")
