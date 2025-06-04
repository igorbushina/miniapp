window.addEventListener("DOMContentLoaded", () => {
  const countrySelect = document.getElementById("country");
  const citySelect = document.getElementById("city");
  const adForm = document.getElementById("adForm");
  const contactInput = document.getElementById("contact");
  const textInput = document.getElementById("text");
  const categorySelect = document.getElementById("category");
  const gdprCheckbox = document.getElementById("gdpr");
  const viewBtn = document.getElementById("viewBtn");
  const addBtn = document.getElementById("addBtn");
  const backBtn = document.getElementById("backBtn");

  // ✅ Проверка окружения
  if (!window.Telegram?.WebApp?.sendData) {
    alert("⚠️ Откройте мини-приложение через Telegram.");
    return;
  }

  // 📍 Заполнение списка стран
  if (typeof countries === "object") {
    Object.keys(countries).sort().forEach((country) => {
      const option = new Option(country, country);
      countrySelect.appendChild(option);
    });
  } else {
    console.error("❌ Ошибка: объект countries не найден.");
  }

  // 📍 Обновление списка городов при выборе страны
  countrySelect.addEventListener("change", () => {
    const selected = countrySelect.value;
    const cities = countries[selected] || [];
    citySelect.innerHTML = ""; // очистка старых опций

    cities.sort().forEach((city) => {
      const option = new Option(city, city);
      citySelect.appendChild(option);
    });
  });

  // 🟢 Первичная инициализация
  countrySelect.dispatchEvent(new Event("change"));

  // 👁 Просмотр объявлений
  viewBtn.addEventListener("click", () => {
    const country = countrySelect.value;
    const city = citySelect.value;

    if (!country || !city) {
      alert("⚠️ Выберите страну и город.");
      return;
    }

    const payload = { action: "view", country, city };
    Telegram.WebApp.sendData(JSON.stringify(payload));
    console.log("📤 View payload:", payload);

    // Открытие ссылки для определённого города
    if (country === "Германия" && city === "Гельдерн") {
      Telegram.WebApp.openTelegramLink("https://t.me/zhivuv_gelderne");
    }
  });

  // ➕ Показ формы
  addBtn.addEventListener("click", () => {
    adForm.style.display = "block";
    viewBtn.style.display = "none";
    addBtn.style.display = "none";
    backBtn.style.display = "block";
  });

  // ⬅️ Назад
  backBtn.addEventListener("click", () => {
    adForm.style.display = "none";
    viewBtn.style.display = "block";
    addBtn.style.display = "block";
    backBtn.style.display = "none";
  });

  // 📤 Отправка формы
  adForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const payload = {
      action: "add",
      country: countrySelect.value,
      city: citySelect.value,
      category: categorySelect.value,
      contact: contactInput.value.trim(),
      text: textInput.value.trim()
    };

    // Валидация данных
    if (
      !payload.country ||
      !payload.city ||
      !payload.category ||
      !payload.contact ||
      !payload.text
    ) {
      alert("⚠️ Заполните все поля.");
      return;
    }

    if (!gdprCheckbox.checked) {
      alert("⚠️ Подтвердите согласие на обработку персональных данных.");
      return;
    }

    Telegram.WebApp.sendData(JSON.stringify(payload));
    console.log("📤 Add payload:", payload);

    adForm.reset();
    adForm.style.display = "none";
    viewBtn.style.display = "block";
    addBtn.style.display = "block";
    backBtn.style.display = "none";

    // Закрытие окна после небольшой задержки
    setTimeout(() => Telegram.WebApp.close(), 400);
  });
});
