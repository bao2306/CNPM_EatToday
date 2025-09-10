from typing import List, Optional
from datetime import datetime
from enum import Enum

class MealType(Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"

class PlanStatus(Enum):
    DRAFT = "draft"
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class UserRole(Enum):
    GUEST = "guest"
    USER = "user"
    ADMIN = "admin"
    NUTRITIONIST = "nutritionist"
    PLANNER = "planner"

class Recipe:
    def __init__(self, id: int, name: str, description: str, ingredients: List[str], 
                 instructions: str, prep_time: int, cook_time: int, servings: int,
                 nutrition_info: dict = None, created_by: int = None, is_public: bool = True):
        self.id = id
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.nutrition_info = nutrition_info or {}
        self.created_by = created_by
        self.is_public = is_public
        self.created_at = datetime.now()

class Ingredient:
    def __init__(self, id: int, name: str, category: str, unit: str, 
                 nutrition_per_100g: dict = None):
        self.id = id
        self.name = name
        self.category = category  # meat, vegetable, grain, dairy, etc.
        self.unit = unit  # kg, g, piece, cup, etc.
        self.nutrition_per_100g = nutrition_per_100g or {}
        self.created_at = datetime.now()

class User:
    def __init__(self, id: int, username: str, email: str, password_hash: str, 
                 role: UserRole = UserRole.USER, family_size: int = 1, 
                 dietary_preferences: List[str] = None, budget: float = 0):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.family_size = family_size
        self.dietary_preferences = dietary_preferences or []
        self.budget = budget
        self.created_at = datetime.now()

class MealPlan:
    def __init__(self, id: int, user_id: int, plan_date: datetime, 
                 status: PlanStatus = PlanStatus.DRAFT, meals: List[dict] = None,
                 total_cost: float = 0, nutrition_summary: dict = None):
        self.id = id
        self.user_id = user_id
        self.plan_date = plan_date
        self.status = status
        self.meals = meals or []  # List of meal objects
        self.total_cost = total_cost
        self.nutrition_summary = nutrition_summary or {}
        self.created_at = datetime.now()

class Meal:
    def __init__(self, id: int, meal_plan_id: int, meal_type: MealType, 
                 recipes: List[int] = None, notes: str = ""):
        self.id = id
        self.meal_plan_id = meal_plan_id
        self.meal_type = meal_type
        self.recipes = recipes or []  # List of recipe IDs
        self.notes = notes
        self.created_at = datetime.now()

class ShoppingList:
    def __init__(self, id: int, user_id: int, meal_plan_id: int, 
                 items: List[dict] = None, total_cost: float = 0, 
                 is_completed: bool = False):
        self.id = id
        self.user_id = user_id
        self.meal_plan_id = meal_plan_id
        self.items = items or []  # List of shopping items
        self.total_cost = total_cost
        self.is_completed = is_completed
        self.created_at = datetime.now()

class ShoppingItem:
    def __init__(self, id: int, shopping_list_id: int, ingredient_name: str, 
                 quantity: float, unit: str, estimated_cost: float = 0, 
                 is_purchased: bool = False):
        self.id = id
        self.shopping_list_id = shopping_list_id
        self.ingredient_name = ingredient_name
        self.quantity = quantity
        self.unit = unit
        self.estimated_cost = estimated_cost
        self.is_purchased = is_purchased
        self.created_at = datetime.now()

class NutritionInfo:
    def __init__(self, calories: float = 0, protein: float = 0, carbs: float = 0, 
                 fat: float = 0, fiber: float = 0, sugar: float = 0, 
                 sodium: float = 0, vitamins: dict = None, minerals: dict = None):
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
        self.sugar = sugar
        self.sodium = sodium
        self.vitamins = vitamins or {}
        self.minerals = minerals or {}
