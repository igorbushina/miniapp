# 🌍 Живу в… — Telegram Mini App

Мини-приложение Telegram, позволяющее публиковать и просматривать объявления по странам, городам и категориям. Все объявления публикуются в единый Telegram-канал с фильтрацией по хэштегам (`#Страна #Город #Категория`).

---

## 📁 Структура проекта

miniapp/
├── city_group_ids.py         # [Необязательный] Маппинг стран и городов
├── data.js                   # Жестко заданный список стран (19) и 50 городов на страну
├── handlers.py               # Telegram-бот: WebApp, публикации, удаление
├── index.html                # Интерфейс Mini App
├── main.py                   # Точка входа и запуск бота
├── README.md                 # Этот файл
├── requirements.txt          # Python-зависимости
├── script.js                 # Вся логика мини-приложения
├── style.css                 # Стилизация интерфейса
└── .env                      # Переменные окружения
---

---

## 🚀 Возможности

- ✅ Выбор страны и города из зафиксированного списка (через `data.js`)
- ✅ Добавление объявления: категория, контакт, текст, фото, GDPR
- ✅ Публикация в Telegram-канал `@ZhivuVChannel`
- ✅ Фильтрация через хэштеги (`#Германия #Берлин #Услуги`)
- ✅ Кнопка просмотра ведёт в канал
- ✅ Стилизация под Telegram, с мобильной адаптацией
- ✅ Хранение данных через Webhook в Google Sheets (опционально)

---

## 🛠️ Установка и запуск

1. **Клонируй репозиторий:**

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

    4.    Запусти проект:
    python main.py
    
    Или задеплой на Render, Vercel или другую платформу.

⸻

🧩 Используемые технологии
    •    python-telegram-bot[webhooks]==20.8
    •    aiohttp
    •    dotenv
    •    HTML5, CSS3, JavaScript
    •    Telegram WebApp SDK

⸻

📦 Интеграции
    •    ✅ Telegram WebApp — интеграция мини-приложения в Telegram-бота
    •    ✅ Make.com Webhook — (опционально) сохранение данных в Google Sheets

⸻

🧹 Удалённые / неиспользуемые модули
    •    get_chat_id.py — встроено в handlers.py
    •    city_group_usernames.py — удалено (отказ от Telegram-групп)

⸻

📬 Обратная связь

Автор: Inna Gorbushina

📩 Telegram-бот: @ZhivuVBot
📢 Канал с объявлениями: @ZhivuVChannel

# fix
