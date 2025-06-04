// 🔧 Страны и города (без России)
const countries = {
  "Германия": [...],  // (твой полный список из 50 городов)
  "США": [...],       // (твой список)
  // Добавь оставшиеся страны по аналогии
};

// 🌍 Элементы
const countrySelect = document.getElementById("country");
const citySelect = document.getElementById("city");
const addButton = document.getElementById("addBtn");
const viewButton = document.getElementById("viewBtn");
const adForm = document.getElementById("adForm");
const categorySelect = document.getElementById("category");
const contactInput = document.getElementById("contact");
const textInput = document.getElementById("text");
const gdprCheckbox = document.getElementById("gdpr");
const backBtn = document.getElementById("backBtn");

// 📌 Заполнение стран
function populateCountries() {
  countrySelect.innerHTML = "<option value='' disabled selected>Выберите страну</option>";
  for (const country in countries) {
    const option = document.createElement("option");
    option.value = country;
    option.textContent = country;
    countrySelect.appendChild(option);
  }
}

// 📌 Заполнение городов
function populateCities(country) {
  citySelect.innerHTML = "<option value='' disabled selected>Выберите город</option>";
  countries[country].forEach(city => {
    const option = document.createElement("option");
    option.value = city;
    option.textContent = city;
    citySelect.appendChild(option);
  });
}

// 🧼 Очистка формы
function resetForm() {
  adForm.style.display = "none";
  categorySelect.value = "";
  contactInput.value = "";
  textInput.value = "";
  gdprCheckbox.checked = false;
}

// 📥 Показ формы
function showForm() {
  adForm.style.display = "block";
}

// 🔘 Обработчики
countrySelect.addEventListener("change", () => {
  const selectedCountry = countrySelect.value;
  populateCities(selectedCountry);
});

addButton.addEventListener("click", () => {
  showForm();
});

backBtn.addEventListener("click", () => {
  resetForm();
});

viewButton.addEventListener("click", () => {
  Telegram.WebApp.openLink("https://t.me/ZhivuVChannel");
});

document.getElementById("submitBtn").addEventListener("click", () => {
  const data = {
    action: "add",
    country: countrySelect.value,
    city: citySelect.value,
    category: categorySelect.value,
    contact: contactInput.value,
    text: textInput.value,
    gdpr: gdprCheckbox.checked
  };

  if (!data.country || !data.city || !data.category || !data.contact || !data.text || !data.gdpr) {
    alert("Пожалуйста, заполните все поля и подтвердите согласие на обработку данных.");
    return;
  }

  Telegram.WebApp.sendData(JSON.stringify(data));
  Telegram.WebApp.close();
});

// ▶️ Инициализация
populateCountries();
resetForm();
