from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Salom 👋 bu sinov uchun yaratilgan bot ishlayapti!")

@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
