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
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from city_group_ids import CITY_GROUP_IDS  # словарь вида {(country, city): chat_id}

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()
WEBAPP_URL = os.getenv("WEBAPP_URL")

if not WEBAPP_URL:
    logger.warning("⚠️ Переменная окружения WEBAPP_URL не установлена.")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("🌍 Живу в…", web_app=WebAppInfo(url=WEBAPP_URL))]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы выбрать страну и город:",
        reply_markup=reply_markup
    )

# Команда /getchatid
async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(
        f"Chat ID: <code>{chat_id}</code>",
        parse_mode="HTML"
    )

# Обработка данных из WebApp
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not update.message or not update.message.web_app_data:
            return

        data = json.loads(update.message.web_app_data.data)
        logger.info(f"[DEBUG] Получены данные WebApp: {data}")

        country = data.get("country")
        city = data.get("city")
        action = data.get("action")
        category = data.get("category")
        contact = data.get("contact")
        text = data.get("text")

        key = (country, city)
        group_id = CITY_GROUP_IDS.get(key)

        if not group_id:
            await update.message.reply_text(
                "⛔ Публикация доступна только для поддерживаемых городов.\n"
                "Сейчас объявления можно размещать только в группе Гельдерна (Германия)."
            )
            return

        if action == "view":
            username = f"zhivuv_{city.lower()}"
            await update.message.reply_text(
                f"Переходите в Telegram-группу для города {city}:",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(f"👥 Группа {city}", url=f"https://t.me/{username}")]
                ])
            )
            return

        elif action == "add":
            if not category or not contact or not text:
                await update.message.reply_text("⛔ Пожалуйста, заполните все поля.")
                return

            post = f"""📍 <b>{city}, {country}</b>
📂 <b>Категория:</b> {category}
👤 <b>Контакты:</b> {contact}
📝 <b>Текст:</b> {text}"""

            context.user_data["last_post"] = {
                "post": post,
                "chat_id": group_id
            }

            await context.bot.send_message(
                chat_id=group_id,
                text=post,
                parse_mode="HTML"
            )

            logger.info(f"[INFO] Объявление опубликовано в группе: {group_id}")

            await update.message.reply_text(
                "✅ Ваше объявление опубликовано в группе.\n"
                "📸 Прикрепите фото, если хотите — я добавлю его к объявлению."
            )

    except Exception as e:
        logger.error("Ошибка в handle_webapp_data", exc_info=True)
        await update.message.reply_text("⚠️ Произошла ошибка при обработке данных.")

# Обработка фото
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = context.user_data.get("last_post")
        if not data:
            await update.message.reply_text("⚠️ Сначала создайте объявление через кнопку 'Живу в…'")
            return

        if not update.message or not update.message.photo:
            await update.message.reply_text("⚠️ Фото не получено.")
            return

        file_id = update.message.photo[-1].file_id

        await context.bot.send_photo(
            chat_id=data["chat_id"],
            photo=file_id,
            caption="📸 Фото к объявлению"
        )

        await update.message.reply_text("✅ Фото прикреплено к объявлению.")
    except Exception as e:
        logger.error("Ошибка в handle_photo", exc_info=True)
        await update.message.reply_text("⚠️ Ошибка при отправке фото.")

# Отправка chat_id при обычных текстах
async def send_chat_id_auto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message and not update.message.web_app_data:
            chat_id = update.effective_chat.id
            await update.message.reply_text(
                f"Chat ID: <code>{chat_id}</code>",
                parse_mode="HTML"
            )
    except Exception as e:
        logger.error("Ошибка в send_chat_id_auto", exc_info=True)

# Регистрация хендлеров
def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getchatid", get_chat_id))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_chat_id_auto))
