# get_chat_id.py

import asyncio
import os
from telegram import Bot
from dotenv import load_dotenv

# ✅ Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ Переменная BOT_TOKEN не установлена в .env")

async def main():
    bot = Bot(token=TOKEN)

    # 🛠 Отключение webhook перед get_updates
    try:
        webhook_info = await bot.get_webhook_info()
        if webhook_info.url:
            print(f"🔌 Webhook найден: {webhook_info.url} — отключаем...")
            await bot.delete_webhook(drop_pending_updates=True)
    except Exception as e:
        print(f"⚠️ Ошибка при удалении webhook: {e}")

    # 📥 Получение обновлений
    try:
        updates = await bot.get_updates(timeout=10)
    except Exception as e:
        print(f"⚠️ Ошибка при получении обновлений: {e}")
        return

    if not updates:
        print("ℹ️ Нет новых обновлений. Напиши что-нибудь боту или добавь его в группу.")
        return

    print("📬 Полученные обновления:")
    for update in updates:
        message = update.message or update.channel_post or update.edited_message
        if message:
            chat = message.chat
            chat_info = f"""
🔹 Chat ID: {chat.id}
🔹 Тип: {chat.type}
🔹 Название: {chat.title or '—'}
🔹 Username: @{chat.username or '—'}
🔹 Отправитель: @{getattr(message.from_user, 'username', '—')}
""".strip()
            print(chat_info)

if __name__ == "__main__":
    asyncio.run(main())
