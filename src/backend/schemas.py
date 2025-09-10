from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str
    fullname: Optional[str] = None  

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    fullname: Optional[str] = None
    preferences: Optional[str] = None
    budget: Optional[float] = None

    class Config:
        orm_mode = True



class RecipeCreate(BaseModel):
    name: str
    description: str
    nutrition: str

class RecipeOut(BaseModel):
    id: int
    name: str
    description: str
    nutrition: str

    class Config:
        orm_mode = True
