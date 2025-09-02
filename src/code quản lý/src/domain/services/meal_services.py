from src.infrastructure.repositories.icourse_repository import ICourseRepository

class MealDomainService:
    def __init__(self, repository: ICourseRepository):
        self.repository = repository

    def get_all_meals(self):
        return self.repository.get_all()

    def add_meal(self, meal):
        return self.repository.add(meal)