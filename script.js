const countryCityMap = {
  "Германия": ["Гельдерн", "Берлин", "Гамбург", "Мюнхен"],
  "Франция": ["Париж", "Марсель"],
  "Италия": ["Рим", "Милан"],
  "США": ["Нью-Йорк", "Лос-Анджелес"],
  "Испания": ["Мадрид", "Барселона"]
};

const countries = Object.keys(countryCityMap).sort();
const countrySelect = document.getElementById("country");
const citySelect = document.getElementById("city");

// Заполнение списка стран
countries.forEach((country) => {
  const option = document.createElement("option");
  option.value = country;
  option.text = country;
  countrySelect.appendChild(option);
});

// Обработка выбора страны
countrySelect.addEventListener("change", function () {
  const selectedCountry = this.value;
  const cities = (countryCityMap[selectedCountry] || []).sort();

  citySelect.innerHTML = "";
  cities.forEach((city) => {
    const option = document.createElement("option");
    option.value = city;
    option.text = city;
    citySelect.appendChild(option);
  });
});

// Инициализация начального списка городов
if (countries.length > 0) {
  countrySelect.value = countries[0];
  const cities = (countryCityMap[countries[0]] || []).sort();
  cities.forEach((city) => {
    const option = document.createElement("option");
    option.value = city;
    option.text = city;
    citySelect.appendChild(option);
  });
}

function submitSelection() {
  const country = document.getElementById("country").value;
  const city = document.getElementById("city").value;
  const category = document.getElementById("category").value;

  const result = {
    country,
    city,
    category
  };

  Telegram.WebApp.sendData(JSON.stringify(result));
  Telegram.WebApp.close();
}

Telegram.WebApp.ready();
Telegram.WebApp.expand();