// 🔧 Элементы
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
const submitBtn = document.getElementById("submitBtn");

// ▶️ Заполнение стран
function populateCountries() {
  countrySelect.innerHTML = "<option value='' disabled selected>Выберите страну</option>";
  Object.keys(window.countries).sort().forEach(country => {
    const option = document.createElement("option");
    option.value = country;
    option.textContent = country;
    countrySelect.appendChild(option);
  });
}

// ▶️ Заполнение городов
function populateCities(country) {
  citySelect.innerHTML = "<option value='' disabled selected>Выберите город</option>";
  if (!window.countries[country]) return;

  window.countries[country].forEach(city => {
    const option = document.createElement("option");
    option.value = city;
    option.textContent = city;
    citySelect.appendChild(option);
  });
}

// ▶️ Очистка формы
function resetForm() {
  adForm.style.display = "none";
  categorySelect.value = "";
  contactInput.value = "";
  textInput.value = "";
  gdprCheckbox.checked = false;
}

// ▶️ Показ формы
function showForm() {
  adForm.style.display = "block";
}

// ▶️ Инициализация
function init() {
  populateCountries();
  resetForm();

  countrySelect.addEventListener("change", () => {
    populateCities(countrySelect.value);
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

  submitBtn.addEventListener("click", () => {
    const data = {
      action: "add",
      country: countrySelect.value,
      city: citySelect.value,
      category: categorySelect.value,
      contact: contactInput.value.trim(),
      text: textInput.value.trim(),
      gdpr: gdprCheckbox.checked
    };

    if (!data.country || !data.city || !data.category || !data.contact || !data.text || !data.gdpr) {
      alert("Пожалуйста, заполните все поля и подтвердите согласие на обработку данных.");
      return;
    }

    Telegram.WebApp.sendData(JSON.stringify(data));
    Telegram.WebApp.close();
  });
}

// ▶️ Старт после загрузки
document.addEventListener("DOMContentLoaded", init);
