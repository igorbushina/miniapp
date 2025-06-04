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

// ▶️ Заполнение городов по стране
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

// ▶️ Очистка формы
function resetForm() {
  adForm.style.display = "none";
  mainButtons.style.display = "flex";
  viewCategoryBlock.style.display = "block";
  adForm.reset();
  submitBtn.disabled = false;
}

// ▶️ Показ формы
function showForm() {
  if (!countrySelect.value || !citySelect.value) {
    alert("Пожалуйста, выберите страну и город.");
    return;
  }

  mainButtons.style.display = "none";
  viewCategoryBlock.style.display = "none";
  adForm.style.display = "flex";
  adForm.scrollIntoView({ behavior: "smooth" });
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

  viewButton.addEventListener("click", () => {
    const country = countrySelect.value;
    const city = citySelect.value;
    const category = document.getElementById("viewCategory").value;

    if (!country || !city) {
      alert("Пожалуйста, выберите страну и город.");
      return;
    }

    const hashCountry = "#" + encodeURIComponent(country);
    const hashCity = "#" + encodeURIComponent(city);
    const hashCategory = category ? "#" + encodeURIComponent(category) : "";

    const finalLink = `https://t.me/ZhivuVChannel?country=${hashCountry}&city=${hashCity}${hashCategory}`;
    Telegram.WebApp.openLink(finalLink);
  });

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

    Telegram.WebApp.sendData(JSON.stringify(data));

    setTimeout(() => {
      Telegram.WebApp.close();
    }, 600);
  });
}

// ▶️ Запуск
document.addEventListener("DOMContentLoaded", init);
