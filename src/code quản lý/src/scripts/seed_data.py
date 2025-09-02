from src.infrastructure.databases.db import SessionLocal
from src.infrastructure.models.meal_model import MealModel
from src.infrastructure.models.user_model import UserModel
from src.infrastructure.models.todo_model import TodoModel
from passlib.context import CryptContext

def seed_initial_data():
    db = SessionLocal()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # Seed users
    users = [
        UserModel(id=1, username="admin", hashed_password=pwd_context.hash("admin123")),
        UserModel(id=2, username="user", hashed_password=pwd_context.hash("user123"))
    ]
    for user in users:
        if not db.query(UserModel).filter(UserModel.username == user.username).first():
            db.add(user)

    # Seed meals
    meals = [
        MealModel(id=1, name="Grilled Chicken Salad", category="Lunch", description="Fresh greens with grilled chicken"),
        MealModel(id=2, name="Pasta Primavera", category="Dinner", description="Pasta with seasonal vegetables"),
        MealModel(id=3, name="Fruit Smoothie", category="Breakfast", description="Blend of fresh fruits and yogurt")
    ]
    for meal in meals:
        if not db.query(MealModel).filter(MealModel.id == meal.id).first():
            db.add(meal)

    # Seed todos
    todos = [
        TodoModel(id=1, meal_id=1, task="Prepare chicken for salad"),
        TodoModel(id=2, meal_id=2, task="Buy vegetables for pasta")
    ]
    for todo in todos:
        if not db.query(TodoModel).filter(TodoModel.id == todo.id).first():
            db.add(todo)

    db.commit()
    db.close()
    print("Initial data seeded successfully")

if __name__ == "__main__":
    seed_initial_data()