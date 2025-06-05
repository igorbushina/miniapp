import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# 🔧 Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.getenv("PORT", 10000))

# 🧾 Логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# ✅ Проверка переменных окружения
if not TOKEN:
    raise ValueError("❌ Переменная BOT_TOKEN не установлена в .env")

if not WEBHOOK_URL or not WEBHOOK_URL.startswith("http"):
    raise ValueError("❌ Переменная WEBHOOK_URL должна начинаться с http/https")

# 🤖 Инициализация приложения
application = ApplicationBuilder().token(TOKEN).build()

# 🔌 Подключение хендлеров
setup_handlers(application)
logger.info("✅ Хендлеры подключены.")

# 🚀 Запуск webhook-сервера
if __name__ == "__main__":
    logger.info(f"🌐 Webhook запускается на порту {PORT}, по адресу {WEBHOOK_URL}")
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
        allowed_updates=["message", "callback_query"]
    )
