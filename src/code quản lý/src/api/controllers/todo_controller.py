from fastapi import HTTPException, Depends
from schemas.schemas import TodoCreate, TodoResponse
from infrastructure.model.todo_model import TodoModel
from sqlalchemy.orm import Session
from infrastructure.database.db import get_db

class TodoController:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = next(db)

    def add_todo(self, todo: TodoCreate) -> TodoResponse:
        todos = self.db.query(TodoModel).all()
        new_id = max([todo.id for todo in todos], default=0) + 1
        db_todo = TodoModel(id=new_id, meal_id=todo.meal_id, task=todo.task)
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def get_all_todos(self) -> list[TodoResponse]:
        return self.db.query(TodoModel).all()