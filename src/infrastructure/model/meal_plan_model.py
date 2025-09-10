from src.infrastructure.database.base import db
from datetime import datetime

class MealPlan(db.Model):
    __tablename__ = 'meal_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    plan_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='draft')  # draft, pending_approval, approved, rejected, in_progress, completed
    total_cost = db.Column(db.Float, default=0.0)
    nutrition_summary = db.Column(db.JSON)  # Total nutrition for the day
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref='meal_plans')
    meals = db.relationship('Meal', backref='meal_plan', cascade='all, delete-orphan')
    shopping_lists = db.relationship('ShoppingList', backref='meal_plan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'plan_date': self.plan_date.isoformat() if self.plan_date else None,
            'status': self.status,
            'total_cost': self.total_cost,
            'nutrition_summary': self.nutrition_summary,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'meals': [meal.to_dict() for meal in self.meals] if self.meals else []
        }

class Meal(db.Model):
    __tablename__ = 'meals'
    
    id = db.Column(db.Integer, primary_key=True)
    meal_plan_id = db.Column(db.Integer, db.ForeignKey('meal_plans.id'), nullable=False)
    meal_type = db.Column(db.String(20), nullable=False)  # breakfast, lunch, dinner, snack
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    meal_recipes = db.relationship('MealRecipe', backref='meal', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'meal_plan_id': self.meal_plan_id,
            'meal_type': self.meal_type,
            'notes': self.notes,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'recipes': [mr.recipe.to_dict() for mr in self.meal_recipes] if self.meal_recipes else []
        }

class MealRecipe(db.Model):
    __tablename__ = 'meal_recipes'
    
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    servings = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'meal_id': self.meal_id,
            'recipe_id': self.recipe_id,
            'servings': self.servings,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
