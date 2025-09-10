from ..model.todo_model import Todo
from ..database.base import db

class TodoRepository:
    def get_all_todos(self):
        return Todo.query.all()

    def get_todo_by_id(self, todo_id):
        return Todo.query.get(todo_id)

    def add_todo(self, todo):
        db.session.add(todo)
        db.session.commit()

    def update_todo(self, todo):
        db.session.merge(todo)
        db.session.commit()