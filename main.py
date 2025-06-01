import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# Загрузка переменных окружения
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.getenv("PORT", 10000))

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Подключаем хендлеры (рекомендуется делать через post_init, но можно и сразу)
    setup_handlers(application)

    # Запуск через webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
        allowed_updates=["message", "callback_query"]
    )

if __name__ == "__main__":
    main()
