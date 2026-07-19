import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from database import init_db, register_user, get_role, set_role

API_TOKEN = "8898843698:AAFfaDkBWwnSoAKqrC53T-Gh7kFYz3Tu27U"
WEBAPP_URL = "https://china-mart-pro.vercel.app/"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await register_user(message.from_user.id)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Перейти в ChinaMart", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])
    await message.answer("Добро пожаловать в ChinaMart. Магазин открыт!", reply_markup=keyboard)
@dp.message(Command("admin"))
async def cmd_admin(message: types.Message):
    await set_role(message.from_user.id, 'seller')
    await message.answer("✅ Статус изменен на Продавец!")

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())