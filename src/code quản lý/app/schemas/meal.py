
from pydantic import BaseModel
from datetime import datetime

class MealCreate(BaseModel):
    meal_name: str

class MealRead(BaseModel):
    id: int
    meal_name: str
    eaten_at: datetime

    class Config:
        from_attributes = True
