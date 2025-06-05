import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# 🔧 Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # https://your-app.onrender.com/webhook
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/webhook")
PORT = int(os.getenv("PORT", 10000))

# 🧾 Логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# ✅ Проверка переменных
if not TOKEN:
    raise ValueError("❌ Переменная BOT_TOKEN не установлена.")
if not WEBHOOK_URL.startswith("http"):
    raise ValueError("❌ WEBHOOK_URL должна начинаться с http/https")

# 🤖 Создание Telegram-приложения
application = ApplicationBuilder().token(TOKEN).build()

# 🔌 Подключение хендлеров
setup_handlers(application)
logger.info("✅ Хендлеры подключены.")

# 🚀 Запуск Webhook сервера (без asyncio.run)
logger.info("🚀 Запуск Telegram-бота...")
application.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL + WEBHOOK_PATH,
    allowed_updates=["message", "callback_query"]
)
