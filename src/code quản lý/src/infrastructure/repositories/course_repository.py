from abc import ABC, abstractmethod
from src.domain.models.course_model import CourseModel

class ICourseRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[CourseModel]:
        pass

    @abstractmethod
    def add(self, course: CourseModel) -> CourseModel:
        pass
