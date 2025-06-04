import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# 🔧 Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 📦 Загрузка переменных из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Пример: https://your-app.onrender.com/webhook
PORT = int(os.getenv("PORT", "10000"))

# ✅ Проверка обязательных переменных
if not BOT_TOKEN:
    raise ValueError("❌ Переменная окружения BOT_TOKEN не установлена.")
if not WEBHOOK_URL:
    raise ValueError("❌ Переменная окружения WEBHOOK_URL не установлена.")

logger.info("🚀 Запуск Telegram-бота...")

# 🧩 Создание приложения Telegram
application = ApplicationBuilder().token(BOT_TOKEN).build()

# 📌 Регистрация хендлеров
setup_handlers(application)

logger.info("✅ Хендлеры подключены.")
logger.info(f"🌐 Webhook запускается на порту {PORT} по адресу {WEBHOOK_URL}")

# 🟢 Запуск webhook-сервера
application.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL,
    allowed_updates=["message", "callback_query"]
)
