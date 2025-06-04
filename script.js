// 🔧 DOM-элементы
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
  countrySelect.innerHTML = "<option value='' selected disabled>Выберите страну</option>";
  const countryList = Object.keys(window.countries).sort();
  countryList.forEach(country => {
    const option = document.createElement("option");
    option.value = country;
    option.textContent = country;
    countrySelect.appendChild(option);
  });
}

// ▶️ Заполнение городов по выбранной стране
function populateCities(country) {
  citySelect.innerHTML = "<option value='' selected disabled>Выберите город</option>";
  const cities = window.countries[country];
  if (!cities) return;

  cities.forEach(city => {
    const option = document.createElement("option");
    option.value = city;
    option.textContent = city;
    citySelect.appendChild(option);
  });

  citySelect.disabled = false;
}

// ▶️ Очистка формы и возврат в главное меню
function resetForm() {
  adForm.style.display = "none";
  categorySelect.value = "";
  contactInput.value = "";
  textInput.value = "";
  gdprCheckbox.checked = false;
  submitBtn.disabled = false;
}

// ▶️ Показ формы объявления
function showForm() {
  if (!countrySelect.value || !citySelect.value) {
    alert("Пожалуйста, выберите страну и город перед добавлением объявления.");
    return;
  }
  adForm.style.display = "block";
}

// ▶️ Основная инициализация
function init() {
  populateCountries();
  resetForm();
  citySelect.disabled = true;

  // Изменение страны
  countrySelect.addEventListener("change", () => {
    populateCities(countrySelect.value);
  });

  // Нажатие "Добавить"
  addButton.addEventListener("click", () => {
    showForm();
  });

  // Назад
  backBtn.addEventListener("click", () => {
    resetForm();
  });

  // Нажатие "Посмотреть"
  viewButton.addEventListener("click", () => {
    Telegram.WebApp.openLink("https://t.me/ZhivuVChannel");
  });

  // Отправка данных
  submitBtn.addEventListener("click", (e) => {
    e.preventDefault();

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

    submitBtn.disabled = true;
    Telegram.WebApp.sendData(JSON.stringify(data));
    Telegram.WebApp.close();
  });
}

// ▶️ Инициализация при загрузке страницы
document.addEventListener("DOMContentLoaded", init);
