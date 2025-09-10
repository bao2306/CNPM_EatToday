from src.infrastructure.database.base import db
from datetime import datetime

class ShoppingList(db.Model):
    __tablename__ = 'shopping_lists'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    meal_plan_id = db.Column(db.Integer, db.ForeignKey('meal_plans.id'))
    total_cost = db.Column(db.Float, default=0.0)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref='shopping_lists')
    items = db.relationship('ShoppingItem', backref='shopping_list', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'meal_plan_id': self.meal_plan_id,
            'total_cost': self.total_cost,
            'is_completed': self.is_completed,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'items': [item.to_dict() for item in self.items] if self.items else []
        }

class ShoppingItem(db.Model):
    __tablename__ = 'shopping_items'
    
    id = db.Column(db.Integer, primary_key=True)
    shopping_list_id = db.Column(db.Integer, db.ForeignKey('shopping_lists.id'), nullable=False)
    ingredient_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    estimated_cost = db.Column(db.Float, default=0.0)
    is_purchased = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'shopping_list_id': self.shopping_list_id,
            'ingredient_name': self.ingredient_name,
            'quantity': self.quantity,
            'unit': self.unit,
            'estimated_cost': self.estimated_cost,
            'is_purchased': self.is_purchased,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
