import os
import logging
import asyncio
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# 🔧 Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # https://your-app.onrender.com/webhook
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/webhook")  # НЕ использовать в ApplicationBuilder
PORT = int(os.getenv("PORT", 10000))

# 🧾 Логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# 🤖 Инициализация приложения
application = ApplicationBuilder().token(TOKEN).build()

# 🔌 Подключение хендлеров
setup_handlers(application)
logger.info("✅ Хендлеры подключены.")

# 🚀 Запуск webhook
async def main():
    logger.info("🚀 Запуск Telegram-бота...")
    await application.bot.set_webhook(url=WEBHOOK_URL + WEBHOOK_PATH)
    logger.info(f"🌐 Webhook установлен: {WEBHOOK_URL + WEBHOOK_PATH}")
    await application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL + WEBHOOK_PATH,
        allowed_updates=["message", "callback_query"]
    )

if __name__ == "__main__":
    asyncio.run(main())
