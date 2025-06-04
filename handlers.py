import os
import json
import logging
from dotenv import load_dotenv
from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
)
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# 🔧 Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🌍 Переменные окружения
load_dotenv()
WEBAPP_URL = os.getenv("WEBAPP_URL")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not WEBAPP_URL:
    logger.warning("⚠️ Переменная WEBAPP_URL не установлена.")
if not CHANNEL_ID:
    raise ValueError("❌ Переменная CHANNEL_ID не установлена в .env")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("🌍 Живу в…", web_app=WebAppInfo(url=WEBAPP_URL))]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Привет! Нажми кнопку ниже, чтобы открыть мини-приложение:",
        reply_markup=markup
    )

# 📦 Обработка WebApp-данных
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not update.message or not update.message.web_app_data:
            return

        data = json.loads(update.message.web_app_data.data)
        logger.info(f"[WebApp] Получено: {data}")

        action = data.get("action")
        country = data.get("country")
        city = data.get("city")
        category = data.get("category")
        contact = data.get("contact")
        text = data.get("text")
        gdpr = data.get("gdpr")

        if country == "Россия":
            await update.message.reply_text("⛔ Публикация из России временно недоступна.")
            return

        if action == "add":
            if not all([country, city, category, contact, text]):
                await update.message.reply_text("⚠️ Пожалуйста, заполните все поля.")
                return

            if not gdpr:
                await update.message.reply_text("⚠️ Вы должны согласиться с обработкой персональных данных (GDPR).")
                return

            hashtags = f"#{country.replace(' ', '')} #{city.replace(' ', '')} #{category.replace(' ', '')}"
            post = (
                f"<b>📍 {city}, {country}</b>\n"
                f"<b>📂 Категория:</b> {category}\n"
                f"<b>👤 Контакт:</b> {contact}\n"
                f"<b>📝 Текст:</b> {text}\n\n"
                f"{hashtags}"
            )

            context.user_data["last_post"] = {
                "post": post,
                "chat_id": CHANNEL_ID
            }

            await context.bot.send_message(
                chat_id=CHANNEL_ID,
                text=post,
                parse_mode="HTML"
            )

            await update.message.reply_text(
                "✅ Объявление опубликовано!\n📸 Теперь вы можете отправить фото, и я прикреплю его к объявлению."
            )

    except Exception as e:
        logger.error("❌ Ошибка при обработке WebApp данных", exc_info=True)
        await update.message.reply_text("⚠️ Ошибка при обработке данных. Попробуйте снова.")

# 📸 Обработка фото
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = context.user_data.get("last_post")
        if not data:
            await update.message.reply_text("⚠️ Сначала опубликуйте текст объявления.")
            return

        if not update.message.photo:
            await update.message.reply_text("⚠️ Фото не получено.")
            return

        photo_id = update.message.photo[-1].file_id

        await context.bot.send_photo(
            chat_id=data["chat_id"],
            photo=photo_id,
            caption=data["post"],
            parse_mode="HTML"
        )

        await update.message.reply_text("📸 Фото успешно добавлено!")
        context.user_data.pop("last_post", None)

    except Exception as e:
        logger.error("❌ Ошибка при добавлении фото", exc_info=True)
        await update.message.reply_text("⚠️ Ошибка при добавлении фото.")

# 💬 Ответ по умолчанию — вывод Chat ID
async def echo_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Ваш Chat ID: <code>{update.effective_chat.id}</code>",
        parse_mode="HTML"
    )

# 🧩 Подключение хендлеров
def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_chat_id))
