# Реєстрація на захід

Це веб-додаток для онлайн-реєстрації учасників на подію.
Проєкт реалізований на FastAPI (бекенд) та HTML + JavaScript (фронтенд) з базовим стилем через CSS.

## Функціонал

* Форма реєстрації з валідацією (email, пароль ≥ 8 символів)
* Перегляд усіх зареєстрованих користувачів
* Отримання користувача за ID
* Видалення користувача
* Отримання випадкової цитати
* Збереження у data.json
* Swagger-документація

## Як запустити локально

### 1. Встановити залежності

```bash
pip install fastapi uvicorn pydantic[email]
```

### 2. Запустити бекенд (FastAPI)

```bash
uvicorn main:app --reload
```

Swagger доступний за адресою:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 3. Запустити фронтенд

Можна через Live Server або:

```bash
cd frontend
python -m http.server 5500
```

Відкрити в браузері:
[http://127.0.0.1:5500](http://127.0.0.1:5500)

## Деплой

* Бекенд (FastAPI): [https://your-backend.onrender.com](https://your-backend.onrender.com)
* Фронтенд (GitHub Pages / Vercel): [https://your-frontend.vercel.app](https://your-frontend.vercel.app)

## Автори
-frontend: Ярещенко Євгеній
-backend: Павліченко Платон
-документація + README.md, керування репозиторієм, розгортання проєкту на хостингу: Іващенко Гліб
