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
  const photoInput = document.getElementById("photo");
  const viewBtn = document.getElementById("viewBtn");
  const addBtn = document.getElementById("addBtn");

  // Кнопка "Назад"
  const backBtn = document.createElement("button");
  backBtn.innerHTML = '<i class="fas fa-arrow-left"></i> Назад';
  backBtn.style.marginTop = "20px";
  backBtn.style.backgroundColor = "#ccc";
  backBtn.style.color = "#000";
  backBtn.style.border = "none";
  backBtn.style.borderRadius = "8px";
  backBtn.style.padding = "12px";
  backBtn.style.fontSize = "1rem";
  backBtn.style.cursor = "pointer";
  backBtn.style.display = "none";
  backBtn.type = "button";
  adForm.parentNode.insertBefore(backBtn, adForm.nextSibling);

  // Заполнение списка стран
  const countryList = Object.keys(countries).sort();
  countryList.forEach(country => {
    const option = document.createElement("option");
    option.value = country;
    option.textContent = country;
    countrySelect.appendChild(option);
  });

  // При выборе страны — обновляем города
  countrySelect.addEventListener("change", () => {
    const cities = countries[countrySelect.value] || [];
    citySelect.innerHTML = "";
    cities.sort().forEach(city => {
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      citySelect.appendChild(option);
    });
  });

  // Стартовое обновление списка городов
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

      // Открытие ссылки (внутри Telegram)
      if (countrySelect.value === "Германия" && citySelect.value === "Гельдерн") {
        Telegram.WebApp.openTelegramLink("https://t.me/zhivuv_gelderne");
      }
    } catch (error) {
      console.error("❌ Ошибка при отправке данных (view):", error);
      alert("Ошибка при открытии группы. Проверьте подключение.");
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

  // Отправка объявления
  adForm.addEventListener("submit", (e) => {
    e.preventDefault();

    if (!Telegram || !Telegram.WebApp || !Telegram.WebApp.sendData) {
      alert("❗ WebApp API недоступен. Запустите через Telegram.");
      return;
    }

    if (!gdprCheckbox.checked) {
      alert("⚠️ Вы должны согласиться с обработкой персональных данных.");
      return;
    }

    const file = photoInput.files[0];
    if (file) {
      alert("📸 Фото нужно прикрепить отдельно после публикации, через Telegram-бота.");
      return;
    }

    const payload = {
      action: "add",
      country: countrySelect.value,
      city: citySelect.value,
      category: categorySelect.value,
      contact: contactInput.value,
      text: textInput.value
    };

    try {
      Telegram.WebApp.sendData(JSON.stringify(payload));
      console.log("📤 Payload sent (add):", payload);
    } catch (error) {
      console.error("❌ Ошибка при отправке объявления:", error);
      alert("Ошибка при публикации объявления.");
    }
  });
});
