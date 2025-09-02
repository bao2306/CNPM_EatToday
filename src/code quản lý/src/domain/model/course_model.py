from pydantic import BaseModel

class CourseModel(BaseModel):
    id: int
    name: str
    category: str
    description: str