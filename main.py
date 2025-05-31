from telegram.ext import ApplicationBuilder
from handlers import setup_handlers
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    setup_handlers(app)  # ← только один аргумент
    app.run_polling()

if __name__ == "__main__":
    main()
