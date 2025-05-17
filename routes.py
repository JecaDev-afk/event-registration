from fastapi import APIRouter, HTTPException
from models import Registration, CreateRegistration
from typing import List
from random import choice
import json
from pathlib import Path

router = APIRouter()

# Шлях до JSON-файлу з "базою даних"
DATA_FILE = Path("data.json")

# Набір випадкових цитат
quotes = [
    "Never stop learning!",
    "Code. Sleep. Repeat.",
    "Debug like a boss."
]

# Завантаження користувачів з JSON-файлу
def load_users() -> List[dict]:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Збереження користувачів у JSON-файл
def save_users(users: List[dict]):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)  # створює директорію, якщо потрібно
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

# Початкове завантаження користувачів у пам'ять
raw_users = load_users()
db: List[Registration] = [Registration(**u) for u in raw_users]
id_counter = max((u["id"] for u in raw_users), default=0) + 1

# === POST /users ===
# Реєстрація нового користувача
@router.post("/users", response_model=Registration)
def register_user(user: CreateRegistration):
    global id_counter
    new_user = Registration(id=id_counter, **user.dict())
    db.append(new_user)
    id_counter += 1
    save_users([u.dict() for u in db])
    return new_user

# === GET /users ===
# Повертає список усіх користувачів
@router.get("/users", response_model=List[Registration])
def get_users():
    return db

# === GET /users/{user_id} ===
# Повертає конкретного користувача за ID
@router.get("/users/{user_id}", response_model=Registration)
def get_user(user_id: int):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Користувача не знайдено")

# === DELETE /users/{user_id} ===
# Видалення користувача за його ID
@router.delete("/users/{user_id}")
def delete_user_by_id(user_id: int):
    global db
    for user in db:
        if user.id == user_id:
            db.remove(user)
            save_users([u.dict() for u in db])
            return {"message": f"Користувача з ID {user_id} видалено"}
    raise HTTPException(status_code=404, detail="Користувача не знайдено")

# === DELETE /users/email/{email} ===
# Видалення користувача за email
@router.delete("/users/email/{email}")
def delete_user_by_email(email: str):
    global db
    for user in db:
        if user.email.lower() == email.lower():  # Порівняння без урахування регістру
            db.remove(user)
            save_users([u.dict() for u in db])
            return {"message": f"Користувача з email {email} видалено"}
    raise HTTPException(status_code=404, detail="Користувача з таким email не знайдено")

# === GET /quote ===
# Повертає випадкову цитату
@router.get("/quote")
def get_quote():
    return {"quote": choice(quotes)}
