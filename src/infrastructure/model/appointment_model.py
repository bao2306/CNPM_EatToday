from src.infrastructure.database.base import db

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    consultant_id = db.Column(db.Integer, db.ForeignKey('consultant.id'))
    appointment_time = db.Column(db.DateTime)