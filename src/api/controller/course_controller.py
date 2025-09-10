from flask import jsonify
from src.domain.model import Course

def get_courses():
    courses = [Course(id=1, name="Khóa học dinh dưỡng", description="Học cách ăn uống lành mạnh")]
    return jsonify({"courses": [c.__dict__ for c in courses]})

def get_course_details(course_id):
    course = Course(id=course_id, name="Khóa học dinh dưỡng", description="Học cách ăn uống lành mạnh")
    return jsonify(course.__dict__) if course.id == course_id else jsonify({"error": "Course not found"}), 404