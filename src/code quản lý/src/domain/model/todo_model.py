from pydantic import BaseModel

class TodoModel(BaseModel):
    id: int
    meal_id: int
    task: str