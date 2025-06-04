import os
import logging
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers
from dotenv import load_dotenv

# Загрузка .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # https://miniapp-xx0j.onrender.com/webhook
PORT = int(os.getenv("PORT", 10000))
WEBHOOK_PATH = "/webhook"  # Render фиксирует endpoint

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if not TOKEN:
    raise ValueError("❌ Переменная BOT_TOKEN не установлена в .env")

if not WEBHOOK_URL:
    raise ValueError("❌ Переменная WEBHOOK_URL не установлена в .env")

# 📦 Создание приложения
application = ApplicationBuilder().token(TOKEN).build()

# ✅ Установка хендлеров
async def on_startup(app):
    setup_handlers(app)
    logger.info("✅ Хендлеры подключены.")
    await app.bot.set_webhook(url=WEBHOOK_URL + WEBHOOK_PATH)
    logger.info(f"🔗 Webhook установлен: {WEBHOOK_URL + WEBHOOK_PATH}")

# 🟢 Запуск сервера
if __name__ == "__main__":
    logger.info(f"🌐 Запуск webhook на {PORT} — {WEBHOOK_PATH}")
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_path=WEBHOOK_PATH,
        post_init=on_startup,
        allowed_updates=["message", "callback_query"]
    )
