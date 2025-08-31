from fastapi import HTTPException, Depends
from schemas.schemas import CourseCreate, CourseResponse
from infrastructure.services.meal_service import MealService
from domain.meal import Meal
from sqlalchemy.orm import Session
from infrastructure.database.db import get_db

class CourseController:
    def __init__(self, db: Session = Depends(get_db)):
        self.service = MealService(db)

    def get_random_meal(self) -> CourseResponse:
        meal = self.service.get_random_meal()
        if not meal:
            raise HTTPException(status_code=404, detail="No meals found")
        return meal

    def add_course(self, course: CourseCreate) -> CourseResponse:
        new_meal = self.service.add_meal(course.name, course.category, course.description)
        return new_meal

    def get_all_courses(self) -> list[CourseResponse]:
        meals = self.service.get_all_meals()
        return meals