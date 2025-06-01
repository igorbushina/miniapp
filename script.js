const countries = {
  "Азербайджан": [
    "Агдам", "Агдаш", "Агджабеди", "Агстафа", "Астара",
    "Баку", "Барда", "Бейлаган", "Балакен", "Гянджа",
    "Гобустан", "Губа", "Горадаг", "Гёйчай", "Гянджа",
    "Закаталы", "Загатала", "Зардоб", "Имирли", "Имишли",
    "Кельбаджар", "Кусары", "Кюрдамир", "Ленкорань", "Мингечаур",
    "Нафталан", "Нахичевань", "Нефтечала", "Огуз", "Саатлы",
    "Сабирабад", "Сальян", "Самух", "Сумгаит", "Тертер",
    "Товуз", "Уджары", "Физули", "Хачмаз", "Ходжавенд",
    "Худат", "Хызы", "Шамкир", "Шарур", "Шеки",
    "Шемаха", "Ширван", "Шуша", "Ярдымлы", "Исмаиллы"
  ],
  "Армения": [
    "Абовян", "Айрум", "Алагёз", "Алаверди", "Ани",
    "Арагац", "Арарат", "Артик", "Армавир", "Артаваз",
    "Арцни", "Аштарак", "Бюрегаван", "Берд", "Вагаршапат",
    "Ванадзор", "Веди", "Гавар", "Гарни", "Геховит",
    "Гехаркуник", "Горис", "Гюмри", "Джермук", "Дилижан",
    "Егвард", "Ерасх", "Ереван", "Ехегнадзор", "Зовун",
    "Иджеван", "Капан", "Маралик", "Масис", "Мартуни",
    "Мецамор", "Ноемберян", "Нор Ачин", "Нор Хачн", "Раздан",
    "Севан", "Сисиан", "Спитак", "Степанаван", "Талин",
    "Ташир", "Чаренцаван", "Цахкадзор", "Шнох", "Ширак"
  ],
  "Германия": [
    "Аугсбург", "Берлин", "Билефельд", "Бонн", "Бохум",
    "Брауншвейг", "Бремен", "Висбаден", "Вольфсбург", "Вупперталь",
    "Ганновер", "Гельзенкирхен", "Гельдерн", "Гера", "Гёттинген",
    "Дортмунд", "Дрезден", "Дюссельдорф", "Зарбрюкен", "Зиген",
    "Кассель", "Кёльн", "Киль", "Кобленц", "Крефельд",
    "Любек", "Майнц", "Мангейм", "Мюнстер", "Мюнхен",
    "Нюрнберг", "Ольденбург", "Потсдам", "Регенсбург", "Росток",
    "Штутгарт", "Фрайбург", "Франкфурт-на-Майне", "Хаген", "Хайльбронн",
    "Хамм", "Хемниц", "Цвиккау", "Эрфурт", "Эссен",
    "Ахен", "Ханау", "Херне", "Золинген", "Ульм"
  ],
    "Грузия": [
      "Ахалцихе", "Ахалкалаки", "Батуми", "Болниси", "Вале",
      "Гардабани", "Гори", "Гурджаани", "Дедоплисцкаро", "Дманиси",
      "Душети", "Зестафони", "Зугдиди", "Каспи", "Кварели",
      "Кобулети", "Лагодехи", "Ланчхути", "Марнеули", "Мартвили",
      "Озургети", "Он", "Поти", "Рустави", "Сагареджо",
      "Самтредиа", "Сенаке", "Сигнахи", "Телави", "Тетри-Цкаро",
      "Ткибули", "Тбилиси", "Ткибули", "Цаленджиха", "Цалки",
      "Цнори", "Цхалтубо", "Цхинвали", "Чакви", "Чиатура",
      "Чохатаури", "Шаумяни", "Шемокмеди", "Шоропани", "Хашури",
      "Хоби", "Хони", "Хуло", "Цителцкаро", "Кутаиси"
    ],
    "Израиль": [
      "Акко", "Арад", "Ашдод", "Ашкелон", "Бат-Ям",
      "Беэр-Шева", "Бней-Брак", "Герцлия", "Гиватаим", "Гуш-Дан",
      "Димона", "Йерухам", "Кармиэль", "Кирьят-Шмона", "Кирьят-Ата",
      "Кирьят-Бялик", "Кирьят-Малахи", "Кирьят-Моцкин", "Кирьят-Ям", "Лод",
      "Маале-Адумим", "Мигдаль", "Модин", "Нагария", "Назрет",
      "Нахалаль", "Нешер", "Нетания", "Нетивот", "Офаким",
      "Пардес-Хана", "Петах-Тиква", "Рамат-Ган", "Рамат-Ха-Шарон", "Реховот",
      "Рош-ха-Аин", "Сдерот", "Тель-Авив", "Тверия", "Ум-эль-Фахм",
      "Хайфа", "Хадера", "Холон", "Шохам", "Явне",
      "Яффо", "Кацрин", "Йокнеам", "Бейт-Шемеш", "Бейт-Ян"
    ],
    // … остальные страны по аналогии
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

  // Проверка и инициализация Telegram WebApp
  if (!window.Telegram || !Telegram.WebApp || !Telegram.WebApp.initDataUnsafe) {
    alert("⚠️ Откройте мини-приложение через Telegram, чтобы отправить объявление.");
    return;
  }

  // Заполнение стран
  const countryList = Object.keys(countries).sort();
  countryList.forEach((country) => {
    const option = document.createElement("option");
    option.value = country;
    option.textContent = country;
    countrySelect.appendChild(option);
  });

  // Заполнение городов при выборе страны
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

  // Первоначальная инициализация
  countrySelect.dispatchEvent(new Event("change"));

  // Кнопка "Посмотреть объявления"
  viewBtn.addEventListener("click", () => {
    const payload = {
      action: "view",
      country: countrySelect.value,
      city: citySelect.value
    };

    try {
      Telegram.WebApp.sendData(JSON.stringify(payload));
      console.log("📤 Payload sent (view):", payload);

      // Переход в группу
      if (payload.country === "Германия" && payload.city === "Гельдерн") {
        Telegram.WebApp.openTelegramLink("https://t.me/zhivuv_gelderne");
      }
    } catch (err) {
      console.error("❌ Ошибка перехода в группу:", err);
      alert("Произошла ошибка при открытии группы.");
    }
  });

  // Кнопка "Добавить объявление"
  addBtn.addEventListener("click", () => {
    adForm.style.display = "block";
    viewBtn.style.display = "none";
    addBtn.style.display = "none";
    backBtn.style.display = "block";
  });

  // Кнопка "Назад"
  backBtn.addEventListener("click", () => {
    adForm.style.display = "none";
    viewBtn.style.display = "block";
    addBtn.style.display = "block";
    backBtn.style.display = "none";
  });

  // Отправка формы
  adForm.addEventListener("submit", (e) => {
    e.preventDefault();

    if (!gdprCheckbox.checked) {
      alert("⚠️ Подтвердите согласие на обработку персональных данных.");
      return;
    }

    const payload = {
      action: "add",
      country: countrySelect.value,
      city: citySelect.value,
      category: categorySelect.value,
      contact: contactInput.value.trim(),
      text: textInput.value.trim()
    };

    // Проверка на пустые поля
    if (!payload.category || !payload.contact || !payload.text) {
      alert("⚠️ Пожалуйста, заполните все обязательные поля.");
      return;
    }

    try {
      Telegram.WebApp.sendData(JSON.stringify(payload));
      console.log("📤 Payload sent (add):", payload);
    } catch (err) {
      console.error("❌ Ошибка отправки:", err);
      alert("Произошла ошибка при отправке объявления.");
    }
  });
});
