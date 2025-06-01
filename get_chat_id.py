import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # Или подставь вручную

async def main():
    bot = Bot(token=TOKEN)
    updates = await bot.get_updates()
    if not updates:
        print("Нет новых обновлений. Отправь боту сообщение или добавь его в группу.")
        return

    for update in updates:
        if update.message:
            chat = update.message.chat
            print(f"Chat ID: {chat.id} | Type: {chat.type} | Title: {chat.title} | Username: {chat.username}")

if __name__ == "__main__":
    asyncio.run(main())
