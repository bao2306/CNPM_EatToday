
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = ""
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str | None = ""

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    full_name: str | None = None
    password: str | None = None
