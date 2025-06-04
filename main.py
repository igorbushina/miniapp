import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# 🔧 Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Пример: https://your-domain.onrender.com/webhook
PORT = int(os.getenv("PORT", 10000))

# 📋 Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Проверка переменных
if not TOKEN:
    raise ValueError("❌ Переменная BOT_TOKEN не установлена в .env")

if not WEBHOOK_URL:
    raise ValueError("❌ Переменная WEBHOOK_URL не установлена в .env")

# 🤖 Инициализация Telegram Application
application = ApplicationBuilder().token(TOKEN).build()

# 🔌 Подключение хендлеров
setup_handlers(application)
logger.info("✅ Хендлеры подключены.")

# 🚀 Запуск Webhook-сервера
if __name__ == "__main__":
    logger.info(f"🌐 Webhook запускается на порту {PORT}, по адресу {WEBHOOK_URL}")
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
        allowed_updates=["message", "callback_query"]
    )
