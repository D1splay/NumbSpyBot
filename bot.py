import logging
import asyncio
import aiogram
from aiogram import types

logging.basicConfig(level=logging.INFO)


with open("token.txt", "r") as file:
    TOKEN = file.read().strip()


with open("msg.txt", "r") as file:
    messages = eval(file.read())

bot = aiogram.Bot(token=TOKEN)
dp = aiogram.Dispatcher(bot)


def is_user_processed(user_id):
    with open("processed_users.txt", "r") as file:
        processed_users = file.read().splitlines()
        return str(user_id) in processed_users


def mark_user_as_processed(user_id):
    with open("processed_users.txt", "a") as file:
        file.write(str(user_id) + "\n")


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):

    if not is_user_processed(message.from_user.id):

        keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard_markup.add(types.KeyboardButton(messages["button"], request_contact=True))
        await message.answer(messages["start.msg"], reply_markup=keyboard_markup)
    else:

        await message.answer(messages["error.start.msg"])


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def on_receive_contact(message: types.Message):
    user_data = {
        "id": message.from_user.id,
        "number": message.contact.phone_number,
        "username": message.from_user.username or ""
    }


    if not is_user_processed(user_data["id"]):

        with open("data.txt", "a") as file:
            file.write("---({})---\n".format(message.date))
            file.write("id: {}\n".format(user_data["id"]))
            file.write("number: {}\n".format(user_data["number"]))
            file.write("username: {}\n".format(user_data["username"]))
            file.write("----------\n")


        await message.answer(messages["successful"], reply_markup=types.ReplyKeyboardRemove())


        mark_user_as_processed(user_data["id"])


        print("Contact successfully saved in data.txt")


        await message.bot.delete_message(message.chat.id, message.message_id)

if __name__ == '__main__':
    asyncio.run(dp.start_polling())
