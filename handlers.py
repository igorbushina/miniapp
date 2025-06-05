import os
import json
import logging
import requests
from dotenv import load_dotenv
from telegram import (
    Update,
    WebAppInfo,
    KeyboardButton,
    ReplyKeyboardMarkup
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
SAVE_AD_WEBHOOK = os.getenv("SAVE_AD_WEBHOOK")

if not WEBAPP_URL:
    logger.warning("⚠️ Переменная WEBAPP_URL не установлена.")
if not CHANNEL_ID:
    raise ValueError("❌ Переменная CHANNEL_ID не установлена в .env")
if not SAVE_AD_WEBHOOK:
    logger.warning("⚠️ Переменная SAVE_AD_WEBHOOK не установлена.")

# 🚀 /start с кнопкой запуска Mini App
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
            logger.warning("⚠️ Нет web_app_data в сообщении.")
            return

        raw_data = update.message.web_app_data.data
        logger.info(f"📥 Получены данные из WebApp: {raw_data}")

        data = json.loads(raw_data)

        action = data.get("action")
        country = data.get("country")
        city = data.get("city")
        category = data.get("category")
        contact = data.get("contact")
        text = data.get("text")
        gdpr = data.get("gdpr")

        if not action:
            await update.message.reply_text("⚠️ Не удалось определить действие.")
            return

        # 🔒 Блокировка по стране
        if country == "Россия":
            await update.message.reply_text("⛔ Публикация из России временно недоступна.")
            return

        if action == "add":
            # 🔍 Проверка обязательных полей
            if not all([country, city, category, contact, text]):
                await update.message.reply_text("⚠️ Пожалуйста, заполните все поля.")
                return

            if not gdpr:
                await update.message.reply_text("⚠️ Подтвердите согласие на обработку персональных данных.")
                return

            hashtags = f"#{country.replace(' ', '')} #{city.replace(' ', '')} #{category.replace(' ', '')}"
            post = (
                f"<b>📍 {city}, {country}</b>\n"
                f"<b>📂 Категория:</b> {category}\n"
                f"<b>👤 Контакт:</b> {contact}\n"
                f"<b>📝 Текст:</b> {text}\n\n"
                f"{hashtags}"
            )

            # Публикация в Telegram
            sent = await context.bot.send_message(
                chat_id=CHANNEL_ID,
                text=post,
                parse_mode="HTML"
            )

            # Сохраняем для прикрепления фото
            context.user_data["last_post"] = {
                "post": post,
                "chat_id": CHANNEL_ID
            }

            # Отправка в Make Webhook
            payload = {
                "user_id": update.effective_user.id,
                "country": country,
                "city": city,
                "category": category,
                "contact": contact,
                "text": text,
                "gdpr": gdpr,
                "channel": CHANNEL_ID,
                "timestamp": update.message.date.isoformat(),
                "message_id": sent.message_id
            }

            try:
                response = requests.post(SAVE_AD_WEBHOOK, json=payload, timeout=5)
                response.raise_for_status()
                logger.info("✅ Данные отправлены в Make Webhook")
            except Exception as e:
                logger.error("❌ Ошибка при отправке в Webhook", exc_info=True)

            await update.message.reply_text(
                "✅ Объявление опубликовано!\n📸 Можете отправить фото — я прикреплю его к объявлению."
            )

    except Exception as e:
        logger.error("❌ Ошибка при обработке WebApp-данных", exc_info=True)
        await update.message.reply_text("⚠️ Произошла ошибка при обработке данных.")

# 📸 Обработка отправки фото
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

        await update.message.reply_text("📸 Фото успешно прикреплено!")
        context.user_data.pop("last_post", None)

    except Exception as e:
        logger.error("❌ Ошибка при добавлении фото", exc_info=True)
        await update.message.reply_text("⚠️ Не удалось прикрепить фото.")

# 🪪 Ответ по умолчанию — вывод Chat ID
async def echo_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Ваш Chat ID: <code>{update.effective_chat.id}</code>",
        parse_mode="HTML"
    )

# 🧩 Регистрация хендлеров
def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_chat_id))
