// 🌍 Список стран и городов (без России)
const countries = {
  "Германия": ["Берлин", "Гамбург", "Мюнхен", "Кёльн", "Франкфурт", "Штутгарт", "Гельдерн", "Дюссельдорф", "Бремен", "Эссен", "Дрезден", "Лейпциг", "Нюрнберг", "Ганновер", "Мангейм", "Карлсруэ", "Бонн", "Висбаден", "Аугсбург", "Дуйсбург", "Регенсбург", "Вольфсбург", "Гиссен", "Гейдельберг", "Дармштадт", "Ульм", "Фрайбург", "Потсдам", "Киль", "Хайльбронн", "Оффенбах", "Бохум", "Билефельд", "Золинген", "Кобленц", "Кассель", "Любек", "Гёттинген", "Трир", "Оснабрюк", "Росток", "Гера", "Фленсбург", "Вупперталь", "Хемниц", "Хаген", "Хайдельберг", "Пфорцхайм", "Цвиккау", "Кайзерслаутерн"],
  "США": ["Нью-Йорк", "Лос-Анджелес", "Чикаго", "Хьюстон", "Финикс", "Филадельфия", "Сан-Антонио", "Сан-Диего", "Даллас", "Сан-Хосе", "Остин", "Джексонвилл", "Сан-Франциско", "Индианаполис", "Колумбус", "Форт-Уэрт", "Шарлотт", "Сиэтл", "Денвер", "Вашингтон", "Бостон", "Эль-Пасо", "Детройт", "Нашвилл", "Портленд", "Мемфис", "Оклахома-Сити", "Лас-Вегас", "Луисвилл", "Балтимор", "Милуоки", "Альбукерке", "Тусон", "Фресно", "Меса", "Сакраменто", "Атланта", "Канзас-Сити", "Колорадо-Спрингс", "Майами", "Роли", "Омаха", "Миннеаполис", "Тампа", "Талса", "Орландо", "Цинциннати", "Арлингтон", "Бейкерсфилд"]
};

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

// ▶️ Заполнение стран
function populateCountries() {
  countrySelect.innerHTML = "<option value='' disabled selected>Выберите страну</option>";
  Object.keys(countries).sort().forEach(country => {
    const option = document.createElement("option");
    option.value = country;
    option.textContent = country;
    countrySelect.appendChild(option);
  });
}

// ▶️ Заполнение городов
function populateCities(country) {
  citySelect.innerHTML = "<option value='' disabled selected>Выберите город</option>";
  countries[country].forEach(city => {
    const option = document.createElement("option");
    option.value = city;
    option.textContent = city;
    citySelect.appendChild(option);
  });
}

// 🔁 Очистка формы
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

// 🎯 Обработчики
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

// ▶️ Инициализация
populateCountries();
resetForm();
