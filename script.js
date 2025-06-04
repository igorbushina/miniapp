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

  // ✅ Проверка окружения Telegram
  if (!window.Telegram?.WebApp?.sendData) {
    alert("⚠️ Откройте мини-приложение через Telegram.");
    return;
  }

  // 📍 Заполнение стран
  if (typeof countries === "object") {
    Object.keys(countries).sort().forEach((country) => {
      const option = new Option(country, country);
      countrySelect.appendChild(option);
    });
  } else {
    console.error("❌ Ошибка: объект countries не определён.");
  }

  // 📍 Обновление городов при выборе страны
  countrySelect.addEventListener("change", () => {
    const selectedCountry = countrySelect.value;
    const cities = countries[selectedCountry] || [];
    citySelect.innerHTML = "";

    cities.sort().forEach((city) => {
      const option = new Option(city, city);
      citySelect.appendChild(option);
    });
  });

  // 🟢 Инициализация при загрузке
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

    if (country === "Германия" && city === "Гельдерн") {
      Telegram.WebApp.openTelegramLink("https://t.me/zhivuv_gelderne");
    } else {
      alert("📌 Просмотр объявлений доступен пока только для Гельдерна.");
    }
  });

  // ➕ Показ формы добавления
  addBtn.addEventListener("click", () => {
    adForm.style.display = "block";
    viewBtn.style.display = "none";
    addBtn.style.display = "none";
    backBtn.style.display = "block";
  });

  // ⬅️ Назад к меню
  backBtn.addEventListener("click", () => {
    adForm.style.display = "none";
    viewBtn.style.display = "block";
    addBtn.style.display = "block";
    backBtn.style.display = "none";
  });

  // 📤 Обработка формы отправки
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

    // Валидация
    if (
      !payload.country ||
      !payload.city ||
      !payload.category ||
      !payload.contact ||
      !payload.text
    ) {
      alert("⚠️ Пожалуйста, заполните все поля.");
      return;
    }

    if (!gdprCheckbox.checked) {
      alert("⚠️ Подтвердите согласие на обработку персональных данных.");
      return;
    }

    Telegram.WebApp.sendData(JSON.stringify(payload));
    console.log("📤 Add payload:", payload);

    // Сброс формы
    adForm.reset();
    adForm.style.display = "none";
    viewBtn.style.display = "block";
    addBtn.style.display = "block";
    backBtn.style.display = "none";

    setTimeout(() => Telegram.WebApp.close(), 400);
  });
});
