import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# 🔧 Загрузка переменных из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Например: https://your-app.onrender.com/webhook
PORT = int(os.getenv("PORT", 10000))

# 🧾 Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# ✅ Проверка переменных окружения
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не установлен.")
if not WEBHOOK_URL or not WEBHOOK_URL.startswith("http"):
    raise ValueError("❌ WEBHOOK_URL должен начинаться с http или https.")

# 🤖 Инициализация Telegram-приложения
application = ApplicationBuilder().token(TOKEN).build()

# 🔌 Регистрация всех хендлеров
setup_handlers(application)
logger.info("✅ Хендлеры подключены.")

# 🚀 Запуск Webhook
async def main():
    logger.info(f"🚀 Запуск Telegram-бота через Webhook на {WEBHOOK_URL}...")
    await application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
        allowed_updates=telegram.ext.defaults.DEFAULT_ALLOWED_UPDATES,
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
