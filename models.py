from pydantic import BaseModel, EmailStr, Field

# Модель для відповіді або збереження користувача (включає ID)
class Registration(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)

# Модель для створення нового користувача (без ID)
class CreateRegistration(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
