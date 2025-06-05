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
const mainButtons = document.getElementById("mainButtons");
const viewCategoryBlock = document.getElementById("viewCategoryBlock");
const viewCategorySelect = document.getElementById("viewCategory");

// ▶️ Заполнение стран
function populateCountries() {
  countrySelect.innerHTML = "<option value='' selected disabled>Выберите страну</option>";
  const countries = Object.keys(window.countries || {}).sort();
  countries.forEach(country => {
    const option = document.createElement("option");
    option.value = country;
    option.textContent = country;
    countrySelect.appendChild(option);
  });
}

// ▶️ Заполнение городов
function populateCities(country) {
  citySelect.innerHTML = "<option value='' selected disabled>Выберите город</option>";
  const cities = window.countries?.[country] || [];
  cities.forEach(city => {
    const option = document.createElement("option");
    option.value = city;
    option.textContent = city;
    citySelect.appendChild(option);
  });

  citySelect.disabled = false;
}

// ▶️ Очистка и возврат к главному экрану
function resetForm() {
  adForm.style.display = "none";
  mainButtons.style.display = "flex";
  viewCategoryBlock.style.display = "block"; // показать только для просмотра

  // Сброс значений формы
  categorySelect.value = "";
  contactInput.value = "";
  textInput.value = "";
  gdprCheckbox.checked = false;

  submitBtn.disabled = false;
  submitBtn.innerText = "Отправить";
}

// ▶️ Показ формы добавления объявления
function showForm() {
  if (!countrySelect.value || !citySelect.value) {
    alert("Пожалуйста, выберите страну и город перед подачей объявления.");
    return;
  }

  mainButtons.style.display = "none";
  viewCategoryBlock.style.display = "none"; // скрыть выбор категории для просмотра
  adForm.style.display = "flex";

  requestAnimationFrame(() => {
    adForm.scrollIntoView({ behavior: "smooth" });
  });
}

// ▶️ Инициализация
function init() {
  populateCountries();
  resetForm();
  citySelect.disabled = true;

  countrySelect.addEventListener("change", () => {
    populateCities(countrySelect.value);
  });

  addButton.addEventListener("click", showForm);
  backBtn.addEventListener("click", resetForm);

  // ▶️ Обработка кнопки "Посмотреть"
  viewButton.addEventListener("click", () => {
    const country = countrySelect.value;
    const city = citySelect.value;
    const category = viewCategorySelect.value;

    if (!country || !city) {
      alert("Пожалуйста, выберите страну и город для просмотра.");
      return;
    }

    const url = `https://t.me/ZhivuVChannel?country=${encodeURIComponent(country)}&city=${encodeURIComponent(city)}${category ? `&category=${encodeURIComponent(category)}` : ""}`;
    Telegram.WebApp.openLink(url);
  });

  // ▶️ Отправка данных из формы
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
    submitBtn.innerText = "Отправка...";

    try {
      Telegram.WebApp.sendData(JSON.stringify(data));
      setTimeout(() => {
        Telegram.WebApp.close();
      }, 600);
    } catch (err) {
      alert("❌ Ошибка при отправке. Попробуйте ещё раз.");
      submitBtn.disabled = false;
      submitBtn.innerText = "Отправить";
    }
  });
}

// ▶️ Старт
document.addEventListener("DOMContentLoaded", init);
