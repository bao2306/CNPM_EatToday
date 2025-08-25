from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    username: str
    password: str
    fullname: str = ""

class UserLogin(BaseModel):
    username: str
    password: str

class RecipeCreate(BaseModel):
    title: str
    detail: str

class RecipeOut(BaseModel):
    id: int
    title: str
    detail: str
    class Config:
        orm_mode = True
