import asyncio
import os
from telegram import Bot, Update
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ Переменная BOT_TOKEN не установлена в .env")

async def main():
    bot = Bot(token=TOKEN)

    try:
        updates = await bot.get_updates()
    except Exception as e:
        print(f"⚠️ Ошибка при получении обновлений: {e}")
        return

    if not updates:
        print("ℹ️ Нет новых обновлений. Отправь боту сообщение или добавь его в группу.")
        return

    print("📬 Полученные обновления:")
    for update in updates:
        message = update.message or update.channel_post
        if message:
            chat = message.chat
            chat_info = f"""
🔹 Chat ID: {chat.id}
🔹 Тип: {chat.type}
🔹 Название: {chat.title or '—'}
🔹 Username: @{chat.username or '—'}
""".strip()
            print(chat_info)

if __name__ == "__main__":
    asyncio.run(main())
