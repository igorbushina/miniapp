import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

# Загрузка переменных окружения
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Например: https://<your-render-subdomain>.onrender.com
WEBHOOK_PATH = f"/{BOT_TOKEN}"
PORT = int(os.getenv("PORT", 8443))
HOST = "0.0.0.0"

async def post_init(application):
    await application.bot.set_webhook(url=WEBHOOK_URL + WEBHOOK_PATH)

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(application)
    application.run_webhook(
        listen=HOST,
        port=PORT,
        webhook_path=WEBHOOK_PATH,
        post_init=post_init,
    )

if __name__ == "__main__":
    main()
