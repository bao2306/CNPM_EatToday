from flask import jsonify, request
from src.infrastructure.model import Recipe, MealPlan, User
from src.infrastructure.database.base import db
from datetime import datetime, date

def analyze_meal_plan_nutrition(meal_plan_id):
    """Phân tích dinh dưỡng của kế hoạch bữa ăn"""
    try:
        meal_plan = MealPlan.query.get(meal_plan_id)
        if not meal_plan:
            return jsonify({"success": False, "error": "Meal plan not found"}), 404
        
        # Tính toán tổng dinh dưỡng từ tất cả các bữa ăn
        total_nutrition = {
            'calories': 0,
            'protein': 0,
            'carbs': 0,
            'fat': 0,
            'fiber': 0,
            'sodium': 0
        }
        
        for meal in meal_plan.meals:
            for meal_recipe in meal.meal_recipes:
                recipe = meal_recipe.recipe
                if recipe.nutrition_info:
                    servings = meal_recipe.servings
                    for nutrient, value in recipe.nutrition_info.items():
                        if nutrient in total_nutrition:
                            total_nutrition[nutrient] += (value * servings)
        
        # Đánh giá dinh dưỡng
        user = User.query.get(meal_plan.user_id)
        family_size = user.family_size if user else 1
        
        # Khuyến nghị dinh dưỡng cơ bản (per person)
        daily_recommendations = {
            'calories': 2000 * family_size,
            'protein': 50 * family_size,  # grams
            'carbs': 250 * family_size,   # grams
            'fat': 65 * family_size,      # grams
            'fiber': 25 * family_size,    # grams
            'sodium': 2300 * family_size  # mg
        }
        
        # Tính phần trăm so với khuyến nghị
        nutrition_analysis = {}
        for nutrient, current in total_nutrition.items():
            recommended = daily_recommendations.get(nutrient, 1)
            percentage = (current / recommended * 100) if recommended > 0 else 0
            
            status = "good"
            if percentage < 80:
                status = "low"
            elif percentage > 120:
                status = "high"
            
            nutrition_analysis[nutrient] = {
                'current': current,
                'recommended': recommended,
                'percentage': round(percentage, 1),
                'status': status
            }
        
        return jsonify({
            "success": True,
            "meal_plan_id": meal_plan_id,
            "family_size": family_size,
            "nutrition_analysis": nutrition_analysis,
            "overall_status": "balanced" if all(
                analysis['status'] == 'good' for analysis in nutrition_analysis.values()
            ) else "needs_attention"
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def suggest_recipe_improvements(recipe_id):
    """Gợi ý cải thiện công thức từ góc độ dinh dưỡng"""
    try:
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return jsonify({"success": False, "error": "Recipe not found"}), 404
        
        suggestions = []
        
        # Phân tích dinh dưỡng hiện tại
        nutrition = recipe.nutrition_info or {}
        
        # Gợi ý dựa trên dinh dưỡng
        if nutrition.get('calories', 0) > 500:
            suggestions.append({
                'type': 'calories',
                'message': 'Công thức có lượng calo cao. Cân nhắc giảm chất béo hoặc đường.',
                'priority': 'medium'
            })
        
        if nutrition.get('protein', 0) < 20:
            suggestions.append({
                'type': 'protein',
                'message': 'Thêm nguồn protein như thịt, cá, đậu để cân bằng dinh dưỡng.',
                'priority': 'high'
            })
        
        if nutrition.get('fiber', 0) < 5:
            suggestions.append({
                'type': 'fiber',
                'message': 'Thêm rau củ hoặc ngũ cốc nguyên hạt để tăng chất xơ.',
                'priority': 'medium'
            })
        
        if nutrition.get('sodium', 0) > 600:
            suggestions.append({
                'type': 'sodium',
                'message': 'Giảm muối và gia vị mặn để tốt cho sức khỏe.',
                'priority': 'high'
            })
        
        # Gợi ý dựa trên nguyên liệu
        ingredients = recipe.ingredients or []
        if not any('rau' in ing.lower() or 'vegetable' in ing.lower() for ing in ingredients):
            suggestions.append({
                'type': 'vegetables',
                'message': 'Thêm rau củ để tăng vitamin và khoáng chất.',
                'priority': 'high'
            })
        
        return jsonify({
            "success": True,
            "recipe_id": recipe_id,
            "suggestions": suggestions,
            "total_suggestions": len(suggestions)
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def create_nutrition_plan(user_id):
    """Tạo kế hoạch dinh dưỡng cho người dùng"""
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "JSON data required"}), 400
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({"success": False, "error": "User not found"}), 404
        
        # Tạo kế hoạch dinh dưỡng dựa trên thông tin người dùng
        family_size = user.family_size
        dietary_preferences = user.dietary_preferences or []
        
        # Tính toán nhu cầu dinh dưỡng
        daily_calories = 2000 * family_size
        daily_protein = 50 * family_size
        daily_carbs = 250 * family_size
        daily_fat = 65 * family_size
        
        # Điều chỉnh theo chế độ ăn
        if 'vegetarian' in dietary_preferences:
            daily_protein *= 1.2  # Tăng protein từ thực vật
        if 'low_carb' in dietary_preferences:
            daily_carbs *= 0.7
            daily_fat *= 1.3
        if 'high_protein' in dietary_preferences:
            daily_protein *= 1.5
        
        nutrition_plan = {
            'user_id': user_id,
            'family_size': family_size,
            'dietary_preferences': dietary_preferences,
            'daily_targets': {
                'calories': daily_calories,
                'protein': daily_protein,
                'carbs': daily_carbs,
                'fat': daily_fat,
                'fiber': 25 * family_size,
                'sodium': 2300 * family_size
            },
            'meal_distribution': {
                'breakfast': 0.25,  # 25% calories
                'lunch': 0.35,      # 35% calories
                'dinner': 0.30,     # 30% calories
                'snacks': 0.10      # 10% calories
            },
            'recommendations': [
                'Ăn đủ 5 phần rau củ mỗi ngày',
                'Uống đủ 2-3 lít nước',
                'Hạn chế đường và muối',
                'Chọn ngũ cốc nguyên hạt'
            ]
        }
        
        return jsonify({
            "success": True,
            "message": "Nutrition plan created successfully",
            "nutrition_plan": nutrition_plan
        }), 201
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def get_nutrition_recommendations():
    """Lấy khuyến nghị dinh dưỡng chung"""
    try:
        recommendations = {
            'general': [
                'Ăn đa dạng các loại thực phẩm',
                'Tăng cường rau củ và trái cây',
                'Chọn protein nạc',
                'Hạn chế chất béo bão hòa',
                'Uống đủ nước'
            ],
            'meal_timing': [
                'Ăn sáng trong vòng 1 giờ sau khi thức dậy',
                'Ăn trưa cách bữa sáng 4-5 giờ',
                'Ăn tối cách bữa trưa 4-5 giờ',
                'Không ăn 2-3 giờ trước khi ngủ'
            ],
            'portion_control': [
                'Sử dụng đĩa nhỏ hơn',
                'Ăn chậm, nhai kỹ',
                'Dừng ăn khi cảm thấy no 80%',
                'Chia nhỏ bữa ăn trong ngày'
            ]
        }
        
        return jsonify({
            "success": True,
            "recommendations": recommendations
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
