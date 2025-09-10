from flask import jsonify, request
from src.infrastructure.model import MealPlan, Meal, MealRecipe, Recipe, ShoppingList, ShoppingItem, User
from src.infrastructure.database.base import db
from datetime import datetime, date, timedelta
from collections import defaultdict

def create_weekly_meal_plan(user_id):
    """Tạo kế hoạch bữa ăn cho cả tuần"""
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "JSON data required"}), 400
        
        start_date = data.get('start_date')
        if not start_date:
            return jsonify({"success": False, "error": "start_date is required"}), 400
        
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        
        # Tạo meal plans cho 7 ngày
        meal_plans = []
        for i in range(7):
            plan_date = start_date + timedelta(days=i)
            
            meal_plan = MealPlan(
                user_id=user_id,
                plan_date=plan_date,
                status='draft'
            )
            
            db.session.add(meal_plan)
            db.session.flush()  # Để lấy ID
            
            # Tạo các bữa ăn cơ bản
            meal_types = ['breakfast', 'lunch', 'dinner']
            for meal_type in meal_types:
                meal = Meal(
                    meal_plan_id=meal_plan.id,
                    meal_type=meal_type
                )
                db.session.add(meal)
            
            meal_plans.append(meal_plan)
        
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Weekly meal plan created successfully",
            "meal_plans": [plan.to_dict() for plan in meal_plans]
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def suggest_recipes_for_meal(meal_id):
    """Gợi ý công thức phù hợp cho bữa ăn"""
    try:
        meal = Meal.query.get(meal_id)
        if not meal:
            return jsonify({"success": False, "error": "Meal not found"}), 404
        
        # Lấy thông tin user để gợi ý phù hợp
        user = User.query.join(MealPlan).filter(MealPlan.id == meal.meal_plan_id).first()
        dietary_preferences = user.dietary_preferences or [] if user else []
        
        # Lấy công thức phù hợp với loại bữa ăn
        query = Recipe.query.filter_by(is_public=True)
        
        # Lọc theo chế độ ăn
        if 'vegetarian' in dietary_preferences:
            # Giả sử có trường dietary_type trong Recipe
            pass  # Cần thêm trường này vào model
        
        # Gợi ý theo loại bữa ăn
        meal_type_suggestions = {
            'breakfast': ['Bánh mì', 'Cháo', 'Trứng', 'Sữa', 'Ngũ cốc'],
            'lunch': ['Cơm', 'Phở', 'Bún', 'Mì', 'Salad'],
            'dinner': ['Cơm', 'Canh', 'Thịt', 'Cá', 'Rau'],
            'snack': ['Trái cây', 'Sữa chua', 'Bánh', 'Nước ép']
        }
        
        keywords = meal_type_suggestions.get(meal.meal_type, [])
        suggested_recipes = []
        
        for keyword in keywords:
            recipes = query.filter(Recipe.name.ilike(f'%{keyword}%')).limit(3).all()
            suggested_recipes.extend(recipes)
        
        # Loại bỏ trùng lặp
        unique_recipes = list({recipe.id: recipe for recipe in suggested_recipes}.values())
        
        return jsonify({
            "success": True,
            "meal_id": meal_id,
            "meal_type": meal.meal_type,
            "suggested_recipes": [recipe.to_dict() for recipe in unique_recipes[:10]]
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def generate_shopping_list(meal_plan_id):
    """Tạo danh sách mua sắm từ kế hoạch bữa ăn"""
    try:
        meal_plan = MealPlan.query.get(meal_plan_id)
        if not meal_plan:
            return jsonify({"success": False, "error": "Meal plan not found"}), 404
        
        # Tạo shopping list mới
        shopping_list = ShoppingList(
            user_id=meal_plan.user_id,
            meal_plan_id=meal_plan_id
        )
        
        db.session.add(shopping_list)
        db.session.flush()
        
        # Thu thập tất cả nguyên liệu từ các công thức
        ingredient_quantities = defaultdict(float)
        
        for meal in meal_plan.meals:
            for meal_recipe in meal.meal_recipes:
                recipe = meal_recipe.recipe
                servings = meal_recipe.servings
                
                if recipe.ingredients:
                    for ingredient in recipe.ingredients:
                        # Giả sử ingredient là dict với name và quantity
                        if isinstance(ingredient, dict):
                            name = ingredient.get('name', '')
                            quantity = ingredient.get('quantity', 0)
                            unit = ingredient.get('unit', 'g')
                        else:
                            # Nếu ingredient là string
                            name = str(ingredient)
                            quantity = 1
                            unit = 'piece'
                        
                        key = f"{name}_{unit}"
                        ingredient_quantities[key] += (quantity * servings)
        
        # Tạo shopping items
        total_cost = 0
        for key, total_quantity in ingredient_quantities.items():
            name, unit = key.rsplit('_', 1)
            estimated_cost = total_quantity * 0.5  # Giả sử 0.5 đơn vị tiền per unit
            total_cost += estimated_cost
            
            shopping_item = ShoppingItem(
                shopping_list_id=shopping_list.id,
                ingredient_name=name,
                quantity=total_quantity,
                unit=unit,
                estimated_cost=estimated_cost
            )
            
            db.session.add(shopping_item)
        
        shopping_list.total_cost = total_cost
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Shopping list generated successfully",
            "shopping_list": shopping_list.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def optimize_meal_plan(meal_plan_id):
    """Tối ưu hóa kế hoạch bữa ăn"""
    try:
        meal_plan = MealPlan.query.get(meal_plan_id)
        if not meal_plan:
            return jsonify({"success": False, "error": "Meal plan not found"}), 404
        
        user = User.query.get(meal_plan.user_id)
        if not user:
            return jsonify({"success": False, "error": "User not found"}), 404
        
        # Phân tích kế hoạch hiện tại
        current_cost = meal_plan.total_cost
        budget = user.budget
        
        # Gợi ý tối ưu hóa
        optimizations = []
        
        if current_cost > budget:
            optimizations.append({
                'type': 'cost_reduction',
                'message': f'Chi phí hiện tại ({current_cost}) vượt ngân sách ({budget}). Gợi ý thay thế một số nguyên liệu đắt tiền.',
                'priority': 'high'
            })
        
        # Kiểm tra cân bằng dinh dưỡng
        total_nutrition = {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0}
        
        for meal in meal_plan.meals:
            for meal_recipe in meal.meal_recipes:
                recipe = meal_recipe.recipe
                servings = meal_recipe.servings
                
                if recipe.nutrition_info:
                    for nutrient, value in recipe.nutrition_info.items():
                        if nutrient in total_nutrition:
                            total_nutrition[nutrient] += (value * servings)
        
        # Gợi ý dinh dưỡng
        family_size = user.family_size
        if total_nutrition['protein'] < 50 * family_size:
            optimizations.append({
                'type': 'nutrition',
                'message': 'Thiếu protein. Gợi ý thêm thịt, cá, đậu vào bữa ăn.',
                'priority': 'medium'
            })
        
        if total_nutrition['calories'] < 1500 * family_size:
            optimizations.append({
                'type': 'nutrition',
                'message': 'Thiếu calo. Gợi ý thêm tinh bột và chất béo lành mạnh.',
                'priority': 'medium'
            })
        
        return jsonify({
            "success": True,
            "meal_plan_id": meal_plan_id,
            "current_cost": current_cost,
            "budget": budget,
            "total_nutrition": total_nutrition,
            "optimizations": optimizations
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def share_meal_plan(meal_plan_id):
    """Chia sẻ kế hoạch bữa ăn với người dùng khác"""
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "JSON data required"}), 400
        
        shared_with_user_id = data.get('shared_with_user_id')
        if not shared_with_user_id:
            return jsonify({"success": False, "error": "shared_with_user_id is required"}), 400
        
        meal_plan = MealPlan.query.get(meal_plan_id)
        if not meal_plan:
            return jsonify({"success": False, "error": "Meal plan not found"}), 404
        
        # Tạo bản sao kế hoạch cho người dùng khác
        shared_meal_plan = MealPlan(
            user_id=shared_with_user_id,
            plan_date=meal_plan.plan_date,
            status='draft',
            total_cost=meal_plan.total_cost,
            nutrition_summary=meal_plan.nutrition_summary
        )
        
        db.session.add(shared_meal_plan)
        db.session.flush()
        
        # Sao chép các bữa ăn
        for meal in meal_plan.meals:
            shared_meal = Meal(
                meal_plan_id=shared_meal_plan.id,
                meal_type=meal.meal_type,
                notes=meal.notes
            )
            
            db.session.add(shared_meal)
            db.session.flush()
            
            # Sao chép các công thức
            for meal_recipe in meal.meal_recipes:
                shared_meal_recipe = MealRecipe(
                    meal_id=shared_meal.id,
                    recipe_id=meal_recipe.recipe_id,
                    servings=meal_recipe.servings
                )
                
                db.session.add(shared_meal_recipe)
        
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Meal plan shared successfully",
            "shared_meal_plan": shared_meal_plan.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500
