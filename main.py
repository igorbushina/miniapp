import os
import logging
import asyncio
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# 🔧 Загрузка .env переменных
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # например, https://your-app.onrender.com
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/webhook")
PORT = int(os.getenv("PORT", 10000))

# 🔍 Проверка переменных
if not TOKEN:
    raise ValueError("❌ Переменная BOT_TOKEN не установлена.")
if not WEBHOOK_URL or not WEBHOOK_URL.startswith("http"):
    raise ValueError("❌ Переменная WEBHOOK_URL должна начинаться с http или https")

# 🧾 Логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# 🤖 Создание Telegram-приложения с webhook_path
application = ApplicationBuilder().token(TOKEN).webhook_path(WEBHOOK_PATH).build()

# 🔌 Регистрация хендлеров
setup_handlers(application)
logger.info("✅ Хендлеры подключены.")

# 🚀 Запуск webhook-сервера
async def main():
    logger.info("🚀 Запуск Telegram-бота...")
    await application.initialize()
    await application.start()
    await application.bot.set_webhook(url=WEBHOOK_URL + WEBHOOK_PATH)
    logger.info(f"🌐 Webhook установлен: {WEBHOOK_URL + WEBHOOK_PATH}")
    await application.updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=WEBHOOK_PATH,
        allowed_updates=["message", "callback_query"]
    )
    await application.updater.wait()

if __name__ == "__main__":
    asyncio.run(main())
