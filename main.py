import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Пример: https://example.onrender.com/webhook
PORT = int(os.getenv("PORT", "10000"))

if not BOT_TOKEN or not WEBHOOK_URL:
    raise ValueError("❌ Не заданы переменные BOT_TOKEN или WEBHOOK_URL")

logger.info("🚀 Запуск Telegram-бота...")

# Создание приложения
application = ApplicationBuilder().token(BOT_TOKEN).build()

# Подключение хендлеров
setup_handlers(application)
logger.info("✅ Хендлеры подключены.")

# Запуск webhook-сервера
logger.info(f"🌐 Webhook запускается на порту {PORT} по адресу {WEBHOOK_URL}")
application.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL,
    allowed_updates=["message", "callback_query"],
    # Рекомендуется: Render использует root path
    path="/"
)
