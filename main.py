import os
import logging
import asyncio
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers
from dotenv import load_dotenv

# Загрузка .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Пример: https://miniapp-xx0j.onrender.com/webhook
WEBHOOK_PATH = "/webhook"
PORT = int(os.getenv("PORT", 10000))

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if not TOKEN:
    raise ValueError("❌ Переменная BOT_TOKEN не установлена в .env")

if not WEBHOOK_URL:
    raise ValueError("❌ Переменная WEBHOOK_URL не установлена в .env")

# Запуск бота
async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Подключаем хендлеры
    setup_handlers(application)
    logger.info("✅ Хендлеры подключены.")

    # Запуск Webhook
    logger.info(f"🌐 Webhook запускается на порту {PORT} по адресу {WEBHOOK_URL}{WEBHOOK_PATH}")
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL + WEBHOOK_PATH,
        url_path=WEBHOOK_PATH,  # ✅ вот правильный аргумент
    )

if __name__ == "__main__":
    asyncio.run(main())
