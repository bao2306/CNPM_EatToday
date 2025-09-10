from src.infrastructure.database.base import db
from datetime import datetime

class Recipe(db.Model):
    __tablename__ = 'recipes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    ingredients = db.Column(db.JSON)  # List of ingredients
    instructions = db.Column(db.Text)
    prep_time = db.Column(db.Integer, default=0)  # minutes
    cook_time = db.Column(db.Integer, default=0)  # minutes
    servings = db.Column(db.Integer, default=1)
    nutrition_info = db.Column(db.JSON)  # Nutrition data
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    is_public = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    creator = db.relationship('User', backref='created_recipes')
    meal_recipes = db.relationship('MealRecipe', backref='recipe')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'servings': self.servings,
            'nutrition_info': self.nutrition_info,
            'created_by': self.created_by,
            'is_public': self.is_public,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
