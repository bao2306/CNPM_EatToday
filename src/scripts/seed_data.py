#!/usr/bin/env python3
"""
Script để tạo dữ liệu mẫu cho ứng dụng Eat Today
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.infrastructure.database.base import db
from src.infrastructure.model import User, Recipe, Ingredient, MealPlan, Meal, MealRecipe
from src.app import create_app
from datetime import datetime, date, timedelta
import hashlib

def create_sample_data():
    """Tạo dữ liệu mẫu"""
    app = create_app()
    
    with app.app_context():
        # Xóa dữ liệu cũ
        db.drop_all()
        db.create_all()
        
        # Tạo users
        users = [
            User(
                username="admin",
                email="admin@eattoday.com",
                password_hash=hashlib.sha256("admin123".encode()).hexdigest(),
                role="admin",
                family_size=1
            ),
            User(
                username="nutritionist1",
                email="nutritionist@eattoday.com",
                password_hash=hashlib.sha256("nutrition123".encode()).hexdigest(),
                role="nutritionist",
                family_size=1
            ),
            User(
                username="planner1",
                email="planner@eattoday.com",
                password_hash=hashlib.sha256("planner123".encode()).hexdigest(),
                role="planner",
                family_size=1
            ),
            User(
                username="user1",
                email="user1@eattoday.com",
                password_hash=hashlib.sha256("user123".encode()).hexdigest(),
                role="user",
                family_size=4,
                dietary_preferences=["vegetarian"],
                budget=1000000
            ),
            User(
                username="user2",
                email="user2@eattoday.com",
                password_hash=hashlib.sha256("user123".encode()).hexdigest(),
                role="user",
                family_size=2,
                dietary_preferences=["low_carb"],
                budget=800000
            )
        ]
        
        for user in users:
            db.session.add(user)
        
        db.session.commit()
        print("✅ Created users")
        
        # Tạo ingredients
        ingredients = [
            Ingredient(
                name="Gạo",
                category="grain",
                unit="kg",
                nutrition_per_100g={
                    "calories": 130,
                    "protein": 2.7,
                    "carbs": 28,
                    "fat": 0.3,
                    "fiber": 0.4
                }
            ),
            Ingredient(
                name="Thịt bò",
                category="meat",
                unit="kg",
                nutrition_per_100g={
                    "calories": 250,
                    "protein": 26,
                    "carbs": 0,
                    "fat": 15,
                    "fiber": 0
                }
            ),
            Ingredient(
                name="Cà chua",
                category="vegetable",
                unit="kg",
                nutrition_per_100g={
                    "calories": 18,
                    "protein": 0.9,
                    "carbs": 3.9,
                    "fat": 0.2,
                    "fiber": 1.2
                }
            ),
            Ingredient(
                name="Hành tây",
                category="vegetable",
                unit="kg",
                nutrition_per_100g={
                    "calories": 40,
                    "protein": 1.1,
                    "carbs": 9.3,
                    "fat": 0.1,
                    "fiber": 1.7
                }
            ),
            Ingredient(
                name="Trứng",
                category="dairy",
                unit="piece",
                nutrition_per_100g={
                    "calories": 155,
                    "protein": 13,
                    "carbs": 1.1,
                    "fat": 11,
                    "fiber": 0
                }
            ),
            Ingredient(
                name="Sữa",
                category="dairy",
                unit="ml",
                nutrition_per_100g={
                    "calories": 42,
                    "protein": 3.4,
                    "carbs": 5,
                    "fat": 1,
                    "fiber": 0
                }
            )
        ]
        
        for ingredient in ingredients:
            db.session.add(ingredient)
        
        db.session.commit()
        print("✅ Created ingredients")
        
        # Tạo recipes
        recipes = [
            Recipe(
                name="Cơm rang thập cẩm",
                description="Món cơm rang ngon với nhiều nguyên liệu",
                ingredients=[
                    {"name": "Gạo", "quantity": 200, "unit": "g"},
                    {"name": "Thịt bò", "quantity": 100, "unit": "g"},
                    {"name": "Cà chua", "quantity": 50, "unit": "g"},
                    {"name": "Hành tây", "quantity": 30, "unit": "g"},
                    {"name": "Trứng", "quantity": 1, "unit": "piece"}
                ],
                instructions="1. Nấu cơm chín\n2. Xào thịt bò\n3. Thêm cà chua và hành tây\n4. Cho cơm vào xào\n5. Đập trứng vào",
                prep_time=15,
                cook_time=20,
                servings=2,
                nutrition_info={
                    "calories": 450,
                    "protein": 25,
                    "carbs": 45,
                    "fat": 18,
                    "fiber": 2
                },
                created_by=1,
                is_public=True
            ),
            Recipe(
                name="Canh chua cá",
                description="Món canh chua truyền thống Việt Nam",
                ingredients=[
                    {"name": "Cá", "quantity": 300, "unit": "g"},
                    {"name": "Cà chua", "quantity": 100, "unit": "g"},
                    {"name": "Dứa", "quantity": 50, "unit": "g"},
                    {"name": "Hành tây", "quantity": 20, "unit": "g"}
                ],
                instructions="1. Làm sạch cá\n2. Nấu nước dùng\n3. Thêm cà chua và dứa\n4. Cho cá vào nấu chín",
                prep_time=20,
                cook_time=25,
                servings=3,
                nutrition_info={
                    "calories": 180,
                    "protein": 22,
                    "carbs": 8,
                    "fat": 6,
                    "fiber": 1.5
                },
                created_by=1,
                is_public=True
            ),
            Recipe(
                name="Trứng chiên",
                description="Món trứng chiên đơn giản",
                ingredients=[
                    {"name": "Trứng", "quantity": 3, "unit": "piece"},
                    {"name": "Hành tây", "quantity": 20, "unit": "g"}
                ],
                instructions="1. Đập trứng vào bát\n2. Thêm hành tây thái nhỏ\n3. Đánh đều\n4. Chiên trên chảo",
                prep_time=5,
                cook_time=10,
                servings=2,
                nutrition_info={
                    "calories": 200,
                    "protein": 15,
                    "carbs": 2,
                    "fat": 15,
                    "fiber": 0.5
                },
                created_by=1,
                is_public=True
            )
        ]
        
        for recipe in recipes:
            db.session.add(recipe)
        
        db.session.commit()
        print("✅ Created recipes")
        
        # Tạo meal plan mẫu
        user1 = User.query.filter_by(username="user1").first()
        if user1:
            meal_plan = MealPlan(
                user_id=user1.id,
                plan_date=date.today(),
                status="draft",
                total_cost=50000
            )
            db.session.add(meal_plan)
            db.session.flush()
            
            # Tạo các bữa ăn
            breakfast = Meal(
                meal_plan_id=meal_plan.id,
                meal_type="breakfast",
                notes="Bữa sáng nhẹ"
            )
            lunch = Meal(
                meal_plan_id=meal_plan.id,
                meal_type="lunch",
                notes="Bữa trưa chính"
            )
            dinner = Meal(
                meal_plan_id=meal_plan.id,
                meal_type="dinner",
                notes="Bữa tối gia đình"
            )
            
            db.session.add_all([breakfast, lunch, dinner])
            db.session.flush()
            
            # Thêm công thức vào bữa ăn
            cơm_rang = Recipe.query.filter_by(name="Cơm rang thập cẩm").first()
            canh_chua = Recipe.query.filter_by(name="Canh chua cá").first()
            trứng_chiên = Recipe.query.filter_by(name="Trứng chiên").first()
            
            if cơm_rang and canh_chua and trứng_chiên:
                meal_recipes = [
                    MealRecipe(meal_id=breakfast.id, recipe_id=trứng_chiên.id, servings=1),
                    MealRecipe(meal_id=lunch.id, recipe_id=cơm_rang.id, servings=2),
                    MealRecipe(meal_id=dinner.id, recipe_id=canh_chua.id, servings=3)
                ]
                
                for mr in meal_recipes:
                    db.session.add(mr)
        
        db.session.commit()
        print("✅ Created sample meal plan")
        
        print("\n🎉 Sample data created successfully!")
        print("\n📋 Test accounts:")
        print("Admin: admin / admin123")
        print("Nutritionist: nutritionist1 / nutrition123")
        print("Planner: planner1 / planner123")
        print("User: user1 / user123")
        print("User: user2 / user123")

if __name__ == "__main__":
    create_sample_data()
