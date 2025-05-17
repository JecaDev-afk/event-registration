from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router

app = FastAPI(
    title="Event Registration API",
    description="API для реєстрації користувачів на захід",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",  # для локальної розробки
        "https://event-registration-liart.vercel.app",
        "https://event-registration-git-main-jecadev-afks-projects.vercel.app",
        "https://event-registration-fz4xn8sio-jecadev-afks-projects.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
