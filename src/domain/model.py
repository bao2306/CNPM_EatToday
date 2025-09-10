from typing import List, Optional
from datetime import datetime

class Course:
    def __init__(self, id: int, name: str, description: str, created_at: datetime = None):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at or datetime.now()

class Todo:
    def __init__(self, id: int, task: str, completed: bool = False, due_date: datetime = None):
        self.id = id
        self.task = task
        self.completed = completed
        self.due_date = due_date or datetime.now()

class User:
    def __init__(self, id: int, username: str, password_hash: str, budget: int = 100):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.budget = budget
        self.preferences = []

class ICourseRepository:
    def get_all_courses(self) -> List[Course]:
        pass

    def get_course_by_id(self, course_id: int) -> Optional[Course]:
        pass

    def add_course(self, course: Course) -> None:
        pass

class ITodoRepository:
    def get_all_todos(self) -> List[Todo]:
        pass

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        pass

    def add_todo(self, todo: Todo) -> None:
        pass

    def update_todo(self, todo: Todo) -> None:
        pass