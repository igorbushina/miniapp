import os
import logging
import requests
from dotenv import load_dotenv
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)
from telegram.error import TelegramError

# 🔧 Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🌍 Переменные окружения
load_dotenv()
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
SAVE_AD_WEBHOOK = os.getenv("SAVE_AD_WEBHOOK")

# 🔢 Состояния диалога
COUNTRY, CITY, CATEGORY, TEXT, CONTACT, GDPR = range(6)

# 📂 Список категорий
CATEGORY_OPTIONS = [
    "Ремонт", "Жилье", "Перевозки", "Помощь по дому",
    "Продам", "Куплю", "Знакомства", "Обучение", "Услуги"
]

# 🟢 Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton("/add"), KeyboardButton("/cancel")],
            [KeyboardButton("/search"), KeyboardButton("/help")]
        ],
        resize_keyboard=True
    )
    await update.message.reply_text(
        "👋 Добро пожаловать! Выберите действие:",
        reply_markup=keyboard
    )

# ❓ Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ Команды:\n"
        "/start — главное меню\n"
        "/add — добавить объявление\n"
        "/cancel — отмена действия\n"
        "/search — поиск по хэштегу"
    )

# ➕ Добавление объявления
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌍 Укажите страну:")
    return COUNTRY

async def set_country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    country = update.message.text.strip()
    if country.lower() == "россия":
        await update.message.reply_text("⛔ Публикация из России временно недоступна.")
        return ConversationHandler.END
    context.user_data["country"] = country
    await update.message.reply_text("🏙 Укажите город:")
    return CITY

async def set_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["city"] = update.message.text.strip()
    keyboard = ReplyKeyboardMarkup(
        [[KeyboardButton(cat)] for cat in CATEGORY_OPTIONS],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await update.message.reply_text("📂 Выберите категорию:", reply_markup=keyboard)
    return CATEGORY

async def set_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["category"] = update.message.text.strip()
    await update.message.reply_text("📝 Введите текст объявления:", reply_markup=ReplyKeyboardRemove())
    return TEXT

async def set_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["text"] = update.message.text.strip()
    await update.message.reply_text("📞 Укажите контакт:")
    return CONTACT

async def set_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["contact"] = update.message.text.strip()
    keyboard = ReplyKeyboardMarkup(
        [[KeyboardButton("✅ Да"), KeyboardButton("❌ Нет")]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await update.message.reply_text(
        "🤖 Подтверждаете согласие на обработку персональных данных?",
        reply_markup=keyboard
    )
    return GDPR

async def set_gdpr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    consent = update.message.text.lower().strip()
    await update.message.reply_text("⏳ Обрабатываем данные...", reply_markup=ReplyKeyboardRemove())

    if "да" not in consent:
        await update.message.reply_text("⛔ Публикация невозможна без согласия.")
        return ConversationHandler.END

    # 📦 Данные
    user_id = update.effective_user.id
    message_date = update.message.date.isoformat()

    country = context.user_data.get("country")
    city = context.user_data.get("city")
    category = context.user_data.get("category")
    text = context.user_data.get("text")
    contact = context.user_data.get("contact")

    hashtags = f"#{country.replace(' ', '')} #{city.replace(' ', '')} #{category.replace(' ', '')}"
    post = (
        f"<b>📍 {city}, {country}</b>\n"
        f"<b>📂 Категория:</b> {category}\n"
        f"<b>👤 Контакт:</b> {contact}\n"
        f"<b>📝 Текст:</b> {text}\n\n"
        f"{hashtags}"
    )

    try:
        sent = await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=post,
            parse_mode="HTML"
        )
    except TelegramError:
        logger.error("❌ Ошибка при публикации в канал", exc_info=True)
        await update.message.reply_text("❌ Не удалось опубликовать. Попробуйте позже.")
        return ConversationHandler.END

    context.user_data["last_post"] = {
        "post": post,
        "chat_id": CHANNEL_ID
    }

    payload = {
        "user_id": user_id,
        "country": country,
        "city": city,
        "category": category,
        "contact": contact,
        "text": text,
        "gdpr": True,
        "channel": CHANNEL_ID,
        "timestamp": message_date,
        "message_id": sent.message_id
    }

    if SAVE_AD_WEBHOOK:
        try:
            response = requests.post(SAVE_AD_WEBHOOK, json=payload, timeout=5)
            response.raise_for_status()
            logger.info("✅ Данные отправлены в Webhook.")
        except requests.RequestException:
            logger.error("❌ Ошибка отправки в Webhook", exc_info=True)

    await update.message.reply_text("✅ Объявление опубликовано!\n📸 Теперь можно отправить фото.")
    return ConversationHandler.END

# 📸 Фото
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = context.user_data.get("last_post")
    if not data:
        await update.message.reply_text("⚠️ Сначала разместите текстовое объявление (/add).")
        return

    photo_id = update.message.photo[-1].file_id
    await context.bot.send_photo(
        chat_id=data["chat_id"],
        photo=photo_id,
        caption=data["post"],
        parse_mode="HTML"
    )
    await update.message.reply_text("📸 Фото прикреплено.")
    context.user_data.pop("last_post", None)

# ❌ Отмена
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚫 Добавление отменено.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

# 🆔 Chat ID
async def echo_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Ваш Chat ID: <code>{update.effective_chat.id}</code>",
        parse_mode="HTML"
    )

# 🔌 Регистрация хендлеров
def setup_handlers(app):
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("add", add)],
        states={
            COUNTRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_country)],
            CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_city)],
            CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_category)],
            TEXT: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_text)],
            CONTACT: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_contact)],
            GDPR: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_gdpr)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(conv_handler)
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_chat_id))
