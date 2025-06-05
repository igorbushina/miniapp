import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# 🔧 Загрузка переменных из .env
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

# ✅ Проверка переменных
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не установлен.")
if not WEBHOOK_URL or not WEBHOOK_URL.startswith("http"):
    raise ValueError("❌ WEBHOOK_URL должен начинаться с http или https.")

# 🤖 Приложение Telegram
application = ApplicationBuilder().token(TOKEN).build()
setup_handlers(application)
logger.info("✅ Хендлеры подключены.")

# 🚀 Прямой запуск Webhook
application.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL
)
