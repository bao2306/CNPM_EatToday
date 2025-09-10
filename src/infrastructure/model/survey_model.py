from src.infrastructure.database.base import db
from datetime import datetime

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    questions = db.Column(db.Text)
    responses = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)