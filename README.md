# 🌍 Живу в… — Telegram Mini App

Мини-приложение для Telegram, позволяющее публиковать и просматривать объявления по странам, городам и категориям. Все публикации направляются в единый Telegram-канал с фильтрацией по хэштегам.

---

## 📁 Структура проекта

miniapp/
├── city_group_ids.py           # [Необязательный] Маппинг стран/городов (может быть удалён)
├── data.js                     # Статичный список стран и городов (50 городов на страну)
├── handlers.py                 # Хендлеры Telegram-бота: старт, WebApp, фото
├── index.html                  # Интерфейс мини-приложения
├── main.py                     # Точка входа, запуск Webhook
├── README.md                   # Этот файл
├── requirements.txt            # Зависимости Python
├── script.js                   # Логика интерфейса Mini App
├── style.css                   # Стилизация Mini App
└── .env                        # Переменные окружения (.env)

---

## 🚀 Возможности

- Выбор страны и города (подгружается из `data.js`)
- Публикация объявления (категория, контакт, текст, фото)
- Поддержка GDPR-согласия
- Автоматическое добавление хэштегов: `#Германия #Гельдерн #Услуги`
- Публикация в канал (переменная `CHANNEL_ID`)
- Webhook-интеграция с Telegram и Make (опционально: сохранение в Google Sheets)

---
🛠️ Установка и запуск

1. Клонируй репозиторий:

```bash
git clone https://github.com/your-username/miniapp.git
cd miniapp

    2.    Установи зависимости:
    pip install -r requirements.txt
    
    3.    Создай .env файл:
    BOT_TOKEN=xxx
WEBHOOK_URL=https://your-app.onrender.com/webhook
WEBAPP_URL=https://your-username.github.io/miniapp
CHANNEL_ID=-100XXXXXXXXX
PORT=10000

4.    Запусти локально или задеплой на Render:
python main.py🧩 Технологии
    •    python-telegram-bot[webhooks]==20.8
    •    aiohttp
    •    dotenv
    •    HTML5, CSS3, JavaScript
    •    Telegram WebApp SDK

⸻

📦 Интеграции
    •    Make.com Webhook — для сохранения объявлений в Google Sheets (если нужно)
    •    Telegram WebApp — мини-приложение доступно через встроенную кнопку бота

⸻

🧹 Удалённые файлы
    •    get_chat_id.py — встроено в handlers.py
    •    city_group_usernames.py — не используется, так как отказались от Telegram-групп

⸻

📬 Связь

Автор: Inna Gorbushina

Telegram-бот: @ZhivuVBot
Канал с объявлениями: @ZhivuVChannel
---

✅ Готов к коммиту. Если хочешь — могу сразу отправить команду для `git add README.md && git commit -m "📄 Обновлен README под новую структуру"`.

Ждёшь?
