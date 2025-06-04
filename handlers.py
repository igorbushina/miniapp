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
from city_group_ids import CITY_GROUP_IDS  # словарь {(country, city): chat_id}

# 🔧 Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 📦 Загрузка переменных окружения
load_dotenv()
WEBAPP_URL = os.getenv("WEBAPP_URL")

if not WEBAPP_URL:
    logger.warning("⚠️ Переменная окружения WEBAPP_URL не установлена.")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("🌍 Живу в…", web_app=WebAppInfo(url=WEBAPP_URL))]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы выбрать страну и город:",
        reply_markup=reply_markup
    )

# /getchatid
async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(
        f"Chat ID: <code>{chat_id}</code>",
        parse_mode="HTML"
    )

# Обработка WebApp данных
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not update.message or not update.message.web_app_data:
            return

        data = json.loads(update.message.web_app_data.data)
        logger.info(f"[DEBUG] Получены WebApp данные: {data}")

        action = data.get("action")
        country = data.get("country")
        city = data.get("city")
        category = data.get("category")
        contact = data.get("contact")
        text = data.get("text")

        key = (country, city)
        group_id = CITY_GROUP_IDS.get(key)

        if not group_id:
            await update.message.reply_text(
                "⛔ Публикация доступна только для поддерживаемых городов.\n"
                "Сейчас доступен только город Гельдерн (Германия)."
            )
            return

        if action == "view":
            username = f"zhivuv_{city.lower()}"
            await update.message.reply_text(
                f"📍 Переходите в группу для города {city}:",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(f"👥 Группа {city}", url=f"https://t.me/{username}")]
                ])
            )
            return

        if action == "add":
            if not all([category, contact, text]):
                await update.message.reply_text("⚠️ Пожалуйста, заполните все поля.")
                return

            post = (
                f"📍 <b>{city}, {country}</b>\n"
                f"📂 <b>Категория:</b> {category}\n"
                f"👤 <b>Контакты:</b> {contact}\n"
                f"📝 <b>Текст:</b> {text}"
            )

            # Сохраняем пост для возможности прикрепления фото
            context.user_data["last_post"] = {
                "post": post,
                "chat_id": group_id
            }

            await context.bot.send_message(
                chat_id=group_id,
                text=post,
                parse_mode="HTML"
            )

            logger.info(f"[INFO] Объявление отправлено в {group_id}")

            await update.message.reply_text(
                "✅ Объявление опубликовано.\n"
                "📸 Пришлите фотографию, если хотите прикрепить её к объявлению."
            )

    except Exception as e:
        logger.error("❌ Ошибка при обработке WebApp данных", exc_info=True)
        await update.message.reply_text("⚠️ Ошибка при обработке данных.")

# Обработка фото
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = context.user_data.get("last_post")
        if not data:
            await update.message.reply_text("⚠️ Сначала опубликуйте объявление через Mini App.")
            return

        if not update.message.photo:
            await update.message.reply_text("⚠️ Не удалось получить фотографию.")
            return

        photo_id = update.message.photo[-1].file_id

        await context.bot.send_photo(
            chat_id=data["chat_id"],
            photo=photo_id,
            caption=data["post"],
            parse_mode="HTML"
        )

        await update.message.reply_text("✅ Фото прикреплено и объявление обновлено.")
        context.user_data.pop("last_post", None)

    except Exception as e:
        logger.error("❌ Ошибка при отправке фото", exc_info=True)
        await update.message.reply_text("⚠️ Ошибка при прикреплении фотографии.")

# Временный Echo chat_id
async def echo_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        chat_id = update.effective_chat.id
        await update.message.reply_text(
            f"Chat ID: <code>{chat_id}</code>",
            parse_mode="HTML"
        )

# Регистрация хендлеров
def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getchatid", get_chat_id))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_chat_id))  # временный
