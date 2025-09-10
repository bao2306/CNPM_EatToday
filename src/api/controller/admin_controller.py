from flask import jsonify, request
from src.infrastructure.model import User, Recipe, Ingredient
from src.infrastructure.database.base import db
from datetime import datetime

def get_all_users():
    """Lấy danh sách tất cả người dùng (Admin only)"""
    try:
        users = User.query.all()
        return jsonify({
            "success": True,
            "users": [user.to_dict() for user in users]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def get_user_by_id(user_id):
    """Lấy thông tin chi tiết người dùng (Admin only)"""
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

def update_user_role(user_id):
    """Cập nhật role của người dùng (Admin only)"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"success": False, "error": "User not found"}), 404
        
        data = request.json
        if not data or 'role' not in data:
            return jsonify({"success": False, "error": "role is required"}), 400
        
        valid_roles = ['user', 'admin', 'nutritionist', 'planner']
        if data['role'] not in valid_roles:
            return jsonify({"success": False, "error": f"Invalid role. Must be one of: {valid_roles}"}), 400
        
        user.role = data['role']
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "User role updated successfully",
            "user": user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def delete_user(user_id):
    """Xóa người dùng (Admin only)"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"success": False, "error": "User not found"}), 404
        
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "User deleted successfully"
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def get_all_recipes():
    """Lấy danh sách tất cả công thức (Admin only)"""
    try:
        recipes = Recipe.query.all()
        return jsonify({
            "success": True,
            "recipes": [recipe.to_dict() for recipe in recipes]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def approve_recipe(recipe_id):
    """Phê duyệt công thức (Admin only)"""
    try:
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return jsonify({"success": False, "error": "Recipe not found"}), 404
        
        recipe.is_public = True
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Recipe approved successfully",
            "recipe": recipe.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def reject_recipe(recipe_id):
    """Từ chối công thức (Admin only)"""
    try:
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return jsonify({"success": False, "error": "Recipe not found"}), 404
        
        recipe.is_public = False
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Recipe rejected successfully",
            "recipe": recipe.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def delete_recipe(recipe_id):
    """Xóa công thức (Admin only)"""
    try:
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return jsonify({"success": False, "error": "Recipe not found"}), 404
        
        db.session.delete(recipe)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Recipe deleted successfully"
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def get_all_ingredients():
    """Lấy danh sách tất cả nguyên liệu (Admin only)"""
    try:
        ingredients = Ingredient.query.all()
        return jsonify({
            "success": True,
            "ingredients": [ingredient.to_dict() for ingredient in ingredients]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def add_ingredient():
    """Thêm nguyên liệu mới (Admin only)"""
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "JSON data required"}), 400
        
        required_fields = ['name', 'category', 'unit']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"success": False, "error": f"{field} is required"}), 400
        
        # Kiểm tra nguyên liệu đã tồn tại
        existing_ingredient = Ingredient.query.filter_by(name=data['name']).first()
        if existing_ingredient:
            return jsonify({"success": False, "error": "Ingredient already exists"}), 400
        
        new_ingredient = Ingredient(
            name=data['name'],
            category=data['category'],
            unit=data['unit'],
            nutrition_per_100g=data.get('nutrition_per_100g', {})
        )
        
        db.session.add(new_ingredient)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Ingredient added successfully",
            "ingredient": new_ingredient.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def get_system_stats():
    """Lấy thống kê hệ thống (Admin only)"""
    try:
        total_users = User.query.count()
        total_recipes = Recipe.query.count()
        total_ingredients = Ingredient.query.count()
        public_recipes = Recipe.query.filter_by(is_public=True).count()
        
        return jsonify({
            "success": True,
            "stats": {
                "total_users": total_users,
                "total_recipes": total_recipes,
                "total_ingredients": total_ingredients,
                "public_recipes": public_recipes,
                "private_recipes": total_recipes - public_recipes
            }
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
