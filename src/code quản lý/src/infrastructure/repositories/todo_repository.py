from abc import ABC, abstractmethod
from src.domain.models.todo_model import TodoModel

class ITodoRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[TodoModel]:
        pass

    @abstractmethod
    def add(self, todo: TodoModel) -> TodoModel:
        pass
