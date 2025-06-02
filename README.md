# 🌍 Telegram Mini App — «Живу в…»

Мини-приложение Telegram и бот для размещения и просмотра объявлений по странам и городам.

---

## 📦 Структура проекта

miniapp/
├── handlers.py         # Логика Telegram-бота
├── main.py             # Запуск бота с Webhook
├── database.py         # (опционально) база данных SQLite
├── .env                # Переменные окружения (не загружается в Git)
├── .env.example        # Шаблон для .env
├── requirements.txt    # Зависимости Python
├── static/             # Фронтенд Mini App
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── data.js

---

## ⚙️ Настройка

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/igorbushina/miniapp.git
cd miniapp

2. Установите зависимости:
pip install -r requirements.txt

3. Создайте файл .env на основе .env.example:
BOT_TOKEN=your-bot-token
WEBHOOK_URL=https://miniapp-xx0j.onrender.com/webhook
WEBAPP_URL=https://igorbushina.github.io/miniapp/
GROUP_ID=-1002509743859
PORT=10000

🚀 Развёртывание на Render
    1.    Загрузите проект на GitHub.
    2.    Создайте новый Web Service на Render.com.
    3.    Укажите:
    •    Runtime: Python 3.10+
    •    Build Command: pip install -r requirements.txt
    •    Start Command: python main.py
    4.    Добавьте переменные окружения из .env.

⸻

🌐 Развёртывание фронтенда (GitHub Pages)
    1.    Папка static/ содержит:
    •    index.html, style.css, script.js, data.js
    2.    Опубликуйте её через GitHub Pages:
    •    Перейдите в Settings → Pages
    •    Выберите ветку и путь /static
    •    Пример: https://igorbushina.github.io/miniapp

⸻

✅ Функциональность
    •    Выбор страны и города
    •    Два сценария:
    •    🔍 Посмотреть объявления → переход в Telegram-группу
    •    ➕ Добавить объявление → ввод категории, текста и контакта
    •    Проверка согласия на обработку данных (GDPR)
    •    Поддержка добавления фото через бота
    •    Публикация разрешена только при выборе:
    •    Германия → Гельдерн

⸻

📍 Пример объявления
📍 Гельдерн, Германия
📂 Категория: Услуги
👤 Контакты: @username
📝 Текст: Предлагаю услуги няни.

🧪 Тестирование

После запуска:
    •    /start — проверка кнопки Mini App
    •    /getchatid — получение chat_id
    •    Проверить публикацию объявления через форму
    •    Проверить отправку фото и прикрепление к последнему объявлению

⸻

📄 Лицензия

MIT License
Автор: Inna Gorbushina

---

