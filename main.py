from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(
    title="Event Registration API",
    description="API для реєстрації користувачів на захід",
    version="1.0.0"
)

#  Налаштування CORS — дозвіл на запити з фронтенду (localhost:5500)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # або ["*"] для всіх
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Підключення роутів
app.include_router(router)

#  Запуск команди (лише якщо запускаєш напряму цей файл)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
