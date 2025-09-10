from src.infrastructure.database.base import db
from datetime import datetime

class CourseRegister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    registered_at = db.Column(db.DateTime, default=datetime.now)