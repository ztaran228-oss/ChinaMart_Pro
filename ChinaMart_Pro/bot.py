import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Твой токен бота
TOKEN = "8898843698:AAFfaDkBWwnSoAKqrC53T-Gh7kFYz3Tu27U"

# Сюда мы потом вставим готовую ссылку, которую выдаст Vercel
WEBAPP_URL = "https://ТВОЯ-ССЫЛКА-VERCEL.vercel.app" 

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    # Создаем кнопку, которая будет открывать наш Mini App
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Открыть Магазин", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])
    
    await message.answer(
        "Привет! Добро пожаловать в **ChinaMart UA**.\n\n"
        "Нажми кнопку ниже, чтобы открыть каталог товаров.",
        reply_markup=kb,
        parse_mode="Markdown"
    )

async def main():
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())