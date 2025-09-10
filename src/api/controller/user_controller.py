from flask import jsonify, request
from src.infrastructure.model import User, Recipe, MealPlan, Meal, MealRecipe, ShoppingList, ShoppingItem
from src.infrastructure.database.base import db
from datetime import datetime, date
import hashlib

def register():
    """Đăng ký tài khoản người dùng"""
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "JSON data required"}), 400
        
        required_fields = ['username', 'email', 'password']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"success": False, "error": f"{field} is required"}), 400
        
        # Kiểm tra username và email đã tồn tại
        existing_user = User.query.filter(
            (User.username == data['username']) | (User.email == data['email'])
        ).first()
        
        if existing_user:
            return jsonify({"success": False, "error": "Username or email already exists"}), 400
        
        # Tạo password hash
        password_hash = hashlib.sha256(data['password'].encode()).hexdigest()
        
        # Tạo user mới
        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=password_hash,
            family_size=data.get('family_size', 1),
            dietary_preferences=data.get('dietary_preferences', []),
            budget=data.get('budget', 0.0)
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "User registered successfully",
            "user": new_user.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def login():
    """Đăng nhập người dùng"""
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "JSON data required"}), 400
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"success": False, "error": "Username and password required"}), 400
        
        # Tìm user
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"success": False, "error": "Invalid credentials"}), 401
        
        # Kiểm tra password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if user.password_hash != password_hash:
            return jsonify({"success": False, "error": "Invalid credentials"}), 401
        
        # Tạo token đơn giản (trong thực tế nên dùng JWT)
        token = f"user_{user.id}_{hashlib.sha256(f'{user.username}{datetime.now()}'.encode()).hexdigest()[:16]}"
        
        return jsonify({
            "success": True,
            "message": "Login successful",
            "token": token,
            "user": user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def get_user_profile(user_id):
    """Lấy thông tin profile người dùng"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"success": False, "error": "User not found"}), 404
        
        return jsonify({
            "success": True,
            "user": user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def update_user_profile(user_id):
    """Cập nhật thông tin profile người dùng"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"success": False, "error": "User not found"}), 404
        
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "JSON data required"}), 400
        
        # Cập nhật các trường có thể thay đổi
        if 'family_size' in data:
            user.family_size = data['family_size']
        if 'dietary_preferences' in data:
            user.dietary_preferences = data['dietary_preferences']
        if 'budget' in data:
            user.budget = data['budget']
        
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Profile updated successfully",
            "user": user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def create_meal_plan(user_id):
    """Tạo kế hoạch bữa ăn mới"""
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "JSON data required"}), 400
        
        plan_date = data.get('plan_date')
        if not plan_date:
            return jsonify({"success": False, "error": "plan_date is required"}), 400
        
        # Tạo meal plan mới
        meal_plan = MealPlan(
            user_id=user_id,
            plan_date=datetime.strptime(plan_date, '%Y-%m-%d').date(),
            status='draft'
        )
        
        db.session.add(meal_plan)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Meal plan created successfully",
            "meal_plan": meal_plan.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def get_user_meal_plans(user_id):
    """Lấy danh sách kế hoạch bữa ăn của người dùng"""
    try:
        meal_plans = MealPlan.query.filter_by(user_id=user_id).order_by(MealPlan.plan_date.desc()).all()
        
        return jsonify({
            "success": True,
            "meal_plans": [plan.to_dict() for plan in meal_plans]
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def add_recipe_to_meal(user_id, meal_id):
    """Thêm công thức vào bữa ăn"""
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "JSON data required"}), 400
        
        recipe_id = data.get('recipe_id')
        servings = data.get('servings', 1)
        
        if not recipe_id:
            return jsonify({"success": False, "error": "recipe_id is required"}), 400
        
        # Kiểm tra meal có thuộc về user không
        meal = Meal.query.join(MealPlan).filter(
            Meal.id == meal_id,
            MealPlan.user_id == user_id
        ).first()
        
        if not meal:
            return jsonify({"success": False, "error": "Meal not found"}), 404
        
        # Thêm recipe vào meal
        meal_recipe = MealRecipe(
            meal_id=meal_id,
            recipe_id=recipe_id,
            servings=servings
        )
        
        db.session.add(meal_recipe)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Recipe added to meal successfully",
            "meal_recipe": meal_recipe.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500
