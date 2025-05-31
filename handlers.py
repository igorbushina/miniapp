import os
import json
from dotenv import load_dotenv
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()
WEBAPP_URL = os.getenv("WEBAPP_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("🌍 Живу в…", web_app=WebAppInfo(url=WEBAPP_URL))]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы открыть Mini App:",
        reply_markup=reply_markup
    )

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = json.loads(update.message.web_app_data.data)
        country = data.get("country")
        city = data.get("city")
        category = data.get("category")
        contact = data.get("contact")
        text = data.get("text")

        if country == "Германия" and city == "Гельдерн":
            channel_link = "https://t.me/GeldernBotChannel"
            await update.message.reply_text(
                f"Ваше объявление будет опубликовано в {channel_link}.\n"
                f"📍 {country}, {city}\n📂 Категория: {category}\n👤 Контакт: {contact}\n📝 Текст: {text}"
            )
            # Здесь можно добавить публикацию в канал через Bot API

        else:
            await update.message.reply_text("🔧 Скоро можно будет размещать объявления и в других городах.")
    except Exception as e:
        print(f"[ОШИБКА] handle_webapp_data: {e}")
        await update.message.reply_text("⚠️ Ошибка при обработке данных.")

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
