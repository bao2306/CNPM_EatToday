from flask import jsonify, request
from src.infrastructure.model import Recipe, Ingredient
from src.infrastructure.database.base import db

def get_public_recipes():
    """Lấy danh sách công thức công khai cho khách vãng lai"""
    try:
        recipes = Recipe.query.filter_by(is_public=True).all()
        return jsonify({
            "success": True,
            "recipes": [recipe.to_dict() for recipe in recipes]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def get_recipe_details(recipe_id):
    """Xem chi tiết công thức"""
    try:
        recipe = Recipe.query.filter_by(id=recipe_id, is_public=True).first()
        if not recipe:
            return jsonify({"success": False, "error": "Recipe not found"}), 404
        
        return jsonify({
            "success": True,
            "recipe": recipe.to_dict()
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def search_recipes():
    """Tìm kiếm công thức theo tên hoặc nguyên liệu"""
    try:
        query = request.args.get('q', '').strip()
        if not query:
            return jsonify({"success": False, "error": "Search query is required"}), 400
        
        # Tìm kiếm theo tên công thức
        recipes = Recipe.query.filter(
            Recipe.is_public == True,
            Recipe.name.ilike(f'%{query}%')
        ).all()
        
        # Tìm kiếm theo nguyên liệu
        ingredient_recipes = Recipe.query.filter(
            Recipe.is_public == True,
            Recipe.ingredients.ilike(f'%{query}%')
        ).all()
        
        # Gộp kết quả và loại bỏ trùng lặp
        all_recipes = list(set(recipes + ingredient_recipes))
        
        return jsonify({
            "success": True,
            "recipes": [recipe.to_dict() for recipe in all_recipes],
            "total": len(all_recipes)
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def get_ingredients():
    """Lấy danh sách nguyên liệu có sẵn"""
    try:
        ingredients = Ingredient.query.all()
        return jsonify({
            "success": True,
            "ingredients": [ingredient.to_dict() for ingredient in ingredients]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def get_recipe_categories():
    """Lấy danh sách danh mục công thức"""
    try:
        # Lấy các danh mục từ nguyên liệu
        categories = db.session.query(Ingredient.category).distinct().all()
        category_list = [cat[0] for cat in categories if cat[0]]
        
        return jsonify({
            "success": True,
            "categories": category_list
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
