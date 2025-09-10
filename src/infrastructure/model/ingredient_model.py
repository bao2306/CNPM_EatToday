from src.infrastructure.database.base import db
from datetime import datetime

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(50), nullable=False)  # meat, vegetable, grain, dairy, etc.
    unit = db.Column(db.String(20), default='g')  # kg, g, piece, cup, etc.
    nutrition_per_100g = db.Column(db.JSON)  # Nutrition data per 100g
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships - removed shopping_items relationship as it's not directly linked
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'unit': self.unit,
            'nutrition_per_100g': self.nutrition_per_100g,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
