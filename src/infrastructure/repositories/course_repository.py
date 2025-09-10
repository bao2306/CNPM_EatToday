from ..model.course_model import Course
from ..database.base import db

class CourseRepository:
    def get_all_courses(self):
        return Course.query.all()

    def get_course_by_id(self, course_id):
        return Course.query.get(course_id)

    def add_course(self, course):
        db.session.add(course)
        db.session.commit()