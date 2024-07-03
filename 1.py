import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import MagicData
from aiogram.utils.markdown import hbold

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6813551745:AAHQnY_aNP0QHF8Q7OydrVdE6t1sJok8Uds")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Ку! {message.from_user.full_name}")

# обработчик команды /subscribers
@dp.message(Command('subs'))
async def cmd_subs(message: types.Message):
    chat_id = '+2YjGWLKpw6FiZjMy'
    chat = await bot.get_chat(chat_id)
    await message.answer(chat.title)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


print("11")