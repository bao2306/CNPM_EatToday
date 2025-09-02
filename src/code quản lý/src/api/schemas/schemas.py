from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class CourseCreate(BaseModel):
    name: str
    category: str
    description: str

class CourseResponse(BaseModel):
    id: int
    name: str
    category: str
    description: str

    class Config:
        from_attributes = True

class TodoCreate(BaseModel):
    meal_id: int
    task: str

class TodoResponse(BaseModel):
    id: int
    meal_id: int
    task: str

    class Config:
        from_attributes = True