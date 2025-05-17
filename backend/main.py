from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router  # бо файл routes.py лежить у backend/

app = FastAPI(
    title="Event Registration API",
    description="API для реєстрації користувачів на захід",
    version="1.0.0"
)

# Налаштування CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключення роутера
app.include_router(router)

# Запуск
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
