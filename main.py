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

# 📦 Загрузка .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_HOST = os.getenv("WEBHOOK_URL")  # Пример: https://your-app.onrender.com
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
PORT = int(os.getenv("PORT", "10000"))

# ✅ Проверка переменных
if not BOT_TOKEN:
    raise ValueError("❌ Переменная окружения BOT_TOKEN не установлена.")
if not WEBHOOK_HOST:
    raise ValueError("❌ Переменная окружения WEBHOOK_URL не установлена.")

logger.info("🚀 Запуск Telegram-бота...")

# 🧩 Инициализация приложения
application = ApplicationBuilder().token(BOT_TOKEN).build()

# 📌 Подключение всех хендлеров
setup_handlers(application)

logger.info("✅ Хендлеры подключены.")
logger.info(f"🌐 Webhook запускается на порту {PORT} по адресу {WEBHOOK_URL}")

# ▶️ Запуск webhook-сервера
application.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_path=WEBHOOK_PATH,
    webhook_url=WEBHOOK_URL,
    allowed_updates=["message", "callback_query"]
)
