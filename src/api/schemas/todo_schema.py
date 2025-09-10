from pydantic import BaseModel

class TodoSchema(BaseModel):
    task: str
    completed: bool = False