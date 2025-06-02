const countries = {
  "Азербайджан": ["Баку"],
  "Армения": ["Ереван"],
  "Германия": ["Гельдерн", "Берлин", "Кёльн", "Дюссельдорф"],
  "Грузия": ["Тбилиси"],
  "Израиль": ["Тель-Авив"]
};

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
    alert("⚠️ Пожалуйста, откройте мини-приложение внутри Telegram.");
    return;
  }

  // 📍 Заполнение списка стран
  Object.keys(countries).sort().forEach((country) => {
    const option = document.createElement("option");
    option.value = country;
    option.textContent = country;
    countrySelect.appendChild(option);
  });

  // 📍 Обновление городов при выборе страны
  countrySelect.addEventListener("change", () => {
    const cities = countries[countrySelect.value] || [];
    citySelect.innerHTML = "";

    cities.sort().forEach((city) => {
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      citySelect.appendChild(option);
    });
  });

  // 🟢 Инициализация городов при загрузке
  countrySelect.dispatchEvent(new Event("change"));

  // 👁 Просмотр объявлений
  viewBtn.addEventListener("click", () => {
    const country = countrySelect.value;
    const city = citySelect.value;

    if (!country || !city) {
      alert("⚠️ Пожалуйста, выберите страну и город.");
      return;
    }

    const payload = { action: "view", country, city };
    Telegram.WebApp.sendData(JSON.stringify(payload));
    console.log("📤 View payload:", payload);

    if (country === "Германия" && city === "Гельдерн") {
      Telegram.WebApp.openTelegramLink("https://t.me/zhivuv_gelderne");
    }
  });

  // ➕ Показ формы добавления
  addBtn.addEventListener("click", () => {
    adForm.style.display = "block";
    viewBtn.style.display = "none";
    addBtn.style.display = "none";
    backBtn.style.display = "block";
  });

  // ⬅️ Возврат к кнопкам
  backBtn.addEventListener("click", () => {
    adForm.style.display = "none";
    viewBtn.style.display = "block";
    addBtn.style.display = "block";
    backBtn.style.display = "none";
  });

  // 📤 Отправка объявления
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

    if (!payload.country || !payload.city || !payload.category || !payload.contact || !payload.text) {
      alert("⚠️ Пожалуйста, заполните все поля.");
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

    setTimeout(() => Telegram.WebApp.close(), 400);
  });
});
