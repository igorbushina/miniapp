import os
import json
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

# Загрузка переменных окружения
load_dotenv()
WEBAPP_URL = os.getenv("WEBAPP_URL")
GROUP_ID = os.getenv("GROUP_ID")  # Пример: "-1002509743859"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🌍 Живу в…", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы выбрать страну и город:",
        reply_markup=reply_markup
    )

# Команда /getchatid
async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"Chat ID: {chat_id}")

# Обработка данных из WebApp
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not update.message or not update.message.web_app_data:
            print("[ОШИБКА] update.message.web_app_data отсутствует")
            await update.message.reply_text("⚠️ Данные из мини-приложения не получены.")
            return

        data = json.loads(update.message.web_app_data.data)
        print("[DEBUG] Получены данные WebApp:", data)

        country = data.get("country")
        city = data.get("city")
        action = data.get("action")
        category = data.get("category")
        contact = data.get("contact")
        text = data.get("text")

        if country == "Германия" and city == "Гельдерн":
            if action == "view":
                await update.message.reply_text(
                    "Переходите в группу с объявлениями для Гельдерна:",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("👥 Группа @zhivuv_gelderne", url="https://t.me/zhivuv_gelderne")]
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
📝 <b>Текст:</b> {text}
"""
                context.user_data["last_post"] = post

                await context.bot.send_message(
                    chat_id=GROUP_ID,
                    text=post,
                    parse_mode="HTML"
                )

                print("[INFO] Объявление отправлено в группу:", GROUP_ID)

                await update.message.reply_text(
                    "✅ Ваше объявление опубликовано в группе.\n"
                    "📸 Прикрепите фотографию, если хотите — я добавлю её к объявлению."
                )
                return

        else:
            await update.message.reply_text(
                "⛔ Публикация возможна только для города Гельдерн (Германия)."
            )

    except Exception as e:
        print(f"[ОШИБКА] handle_webapp_data: {e}")
        await update.message.reply_text("⚠️ Произошла ошибка при обработке данных.")

# Обработка фото
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if "last_post" not in context.user_data:
            await update.message.reply_text("⚠️ Пожалуйста, сначала создайте объявление через кнопку 'Живу в…'")
            return

        photo = update.message.photo[-1]
        file_id = photo.file_id

        await context.bot.send_photo(
            chat_id=GROUP_ID,
            photo=file_id,
            caption="📸 Фото к объявлению"
        )

        await update.message.reply_text("✅ Фото прикреплено к объявлению.")
    except Exception as e:
        print(f"[ОШИБКА] handle_photo: {e}")
        await update.message.reply_text("⚠️ Ошибка при отправке фото.")

# Регистрация всех хендлеров
def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getchatid", get_chat_id))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
