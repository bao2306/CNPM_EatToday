from src.infrastructure.database.base import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='user')  # guest, user, admin, nutritionist, planner
    family_size = db.Column(db.Integer, default=1)
    dietary_preferences = db.Column(db.JSON)  # List of dietary preferences
    budget = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'family_size': self.family_size,
            'dietary_preferences': self.dietary_preferences,
            'budget': self.budget,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }