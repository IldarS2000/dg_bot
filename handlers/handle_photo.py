import os
from aiogram import types
from bot import dp
from tag_generator import TAG_GENERATOR
from description_generator import DESCRIPTION_GENERATOR


@dp.message_handler(state="*", content_types=types.ContentTypes.PHOTO)
async def cmd_handle_photo(message: types.Message):
    await message.answer("need wait about 30 second")

    cmd_handle_photo.IMAGE_COUNTER += 1
    if cmd_handle_photo.IMAGE_COUNTER == 1000:
        cmd_handle_photo.IMAGE_COUNTER = 0

    image_path = os.path.join("..", "images", f"image{cmd_handle_photo.IMAGE_COUNTER}.jpg")
    await message.photo[-1].download(image_path)

    object_names = TAG_GENERATOR.detect_objects(image_path)
    description = DESCRIPTION_GENERATOR.generate_description(image_path)

    result = ""
    for object_name in object_names:
        result += f"#{str(object_name)} "
    result += f"\n{description}"
    if result == "":
        await message.answer("nothing detected")
    else:
        await message.answer(result)


cmd_handle_photo.IMAGE_COUNTER = 0
