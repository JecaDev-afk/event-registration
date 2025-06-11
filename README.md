# Event Registration API

Це веб-застосунок для реєстрації користувачів на захід. Реалізовано на базі FastAPI (бекенд) та HTML/JS (фронтенд). Користувачі можуть зареєструватися, отримати випадкову мотиваційну цитату або видалити себе за email.

## Функціонал

* Форма реєстрації з валідацією (email, пароль ≥ 8 символів)
* API для створення, отримання, видалення користувачів
* Випадкові цитати через API
* Swagger-документація на /docs

## Деплой

* Бекенд (FastAPI): [https://event-registration-xbwm.onrender.com](https://event-registration-xbwm.onrender.com)
* Фронтенд (Vercel): [https://event-registration-eight-pearl.vercel.app](https://event-registration-eight-pearl.vercel.app)

## Як запустити локально

### 1. Клонувати репозиторій

Bash

git clone https://github.com/ІМЯ_КОРИСТУВАЧА/event-registration.git
cd event-registration

### 2. Встановити залежності

Bash

pip install -r requirements.txt

### 3. Запустити бекенд

Bash

uvicorn main:app --reload

### 4. Відкрити фронтенд

Відкрий frontend/index.html у браузері (двічі клікни або запусти через Live Server).

---

## Структура проєкту

event-registration/
├── backend/
│   ├── main.py          # Запуск FastAPI
│   ├── routes.py        # API маршрути
│   ├── models.py        # Pydantic-моделі
│   └── data.json        # Зберігання користувачів
│
├── frontend/
│   ├── index.html       # Інтерфейс
│   ├── style.css        # Стилі
│   └── app.js           # Взаємодія з API
│
├── requirements.txt     # Залежності Python
└── README.md

## Приклади API

* POST /users — реєстрація
* DELETE /users/email/{email} — видалення за email
* GET /quote — випадкова цитата

---

Проєкт створено для демонстрації CRUD API з фронтом, деплоєм і документацією.

## Автори
-frontend: Ярещенко Євгеній
-backend: Павліченко Платон
-документація + README.md, керування репозиторієм, розгортання проєкту на хостингу: Іващенко Гліб



посхалко
посхалко
