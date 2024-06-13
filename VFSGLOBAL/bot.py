from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from check_slots import main as check_slots_main
from config import TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для мониторинга свободных слотов на сайте визового центра Болгарии. Используйте команду /check для проверки доступных слотов.")

@dp.message_handler(commands=['check'])
async def check_slots_handler(message: types.Message):
    result = check_slots_main()  # Вызов функции проверки слотов
    await message.reply(f"Результат проверки: {result}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
