import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

BOT_TOKEN = "8376747809:AAFfs87vhDGW2UGz7IQ_of7Fr9tPhpsnMVQ"

# ВАЖНО: Замените на ваш реальный URL от ngrok или хостинга
WEB_APP_URL = "https://gristly-unshirred-kimberley.ngrok-free.dev"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# /start - отправляем кнопку для запуска Mini App
@dp.message(F.text == "/start")
async def start(msg: Message):
    # Создаём клавиатуру с кнопкой Web App
    kb = ReplyKeyboardBuilder()
    kb.button(
        text="🚭 Открыть чат-рулетку",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    
    await msg.answer(
        "👋 Добро пожаловать в чат-рулетку \"Бросаю курить\"!\n\n"
        "Здесь вы найдёте поддержку от людей с похожим опытом.\n\n"
        "Нажмите кнопку ниже, чтобы начать:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )

# Обработчик данных из Mini App
@dp.message(F.web_app_data)
async def webapp_handler(msg: Message):
    action = msg.web_app_data.data
    print("📱 WEBAPP DATA:", action)
    
    if action == "find":
        await msg.answer("🔍 Ищем вам собеседника...")
    else:
        await msg.answer(f"✅ Получил действие: {action}")

async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())