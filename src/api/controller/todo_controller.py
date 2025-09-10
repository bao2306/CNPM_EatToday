from flask import jsonify, request
from src.domain.model import Todo
from datetime import datetime

def get_todos():
    todos = [Todo(id=1, task="Tạo kế hoạch chi tiết", due_date=datetime(2025, 9, 11))]
    return jsonify({"todos": [t.__dict__ for t in todos]})

def add_todo():
    data = request.json
    todo = Todo(id=1, task=data.get('task'), due_date=datetime.now())
    return jsonify({"message": f"Added todo: {todo.task}", "todo": todo.__dict__})