import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

from handlers import setup_handlers

# 🔧 Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 📦 Загрузка .env переменных
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Пример: https://your-app.onrender.com/webhook
PORT = int(os.getenv("PORT", "10000"))

if not BOT_TOKEN:
    raise ValueError("❌ Переменная окружения BOT_TOKEN не установлена.")
if not WEBHOOK_URL:
    raise ValueError("❌ Переменная окружения WEBHOOK_URL не установлена.")
if not PORT:
    raise ValueError("❌ Переменная окружения PORT не установлена.")

logger.info("🚀 Запуск Telegram-бота...")

# 🚀 Запускаем приложение
application = ApplicationBuilder().token(BOT_TOKEN).build()
setup_handlers(application)

logger.info("✅ Хендлеры подключены.")
logger.info(f"🌐 Webhook запускается на порту {PORT} по адресу {WEBHOOK_URL}")

# 🟢 Запуск Webhook (без аргумента 'path'!)
application.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL,
    allowed_updates=["message", "callback_query"]
)
