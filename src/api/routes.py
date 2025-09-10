from flask import Blueprint, jsonify
from .controller.guest_controller import get_public_recipes, get_recipe_details, search_recipes, get_ingredients, get_recipe_categories
from .controller.user_controller import register, login, get_user_profile, update_user_profile, create_meal_plan, get_user_meal_plans, add_recipe_to_meal
from .controller.admin_controller import get_all_users, get_user_by_id, update_user_role, delete_user, get_all_recipes, approve_recipe, reject_recipe, delete_recipe, get_all_ingredients, add_ingredient, get_system_stats
from .controller.nutritionist_controller import analyze_meal_plan_nutrition, suggest_recipe_improvements, create_nutrition_plan, get_nutrition_recommendations
from .controller.planner_controller import create_weekly_meal_plan, suggest_recipes_for_meal, generate_shopping_list, optimize_meal_plan, share_meal_plan
from .middleware import require_json, require_auth, require_role
from . import api_bp

@api_bp.route('/', methods=['GET'])
def home():
    """
    API root endpoint
    ---
    tags:
      - General
    responses:
      200:
        description: Welcome message for API
        schema:
          type: object
          properties:
            message:
              type: string
              example: Welcome to Eat Today API
            actors:
              type: array
              items:
                type: string
              example: ["Guest", "User", "Admin", "Nutritionist", "Planner"]
    """
    return {
        "message": "Welcome to Eat Today API - Meal Planning System",
        "actors": ["Guest", "User", "Admin", "Nutritionist", "Planner"],
        "version": "2.0"
    }, 200

# ==================== GUEST ROUTES (Khách vãng lai) ====================

@api_bp.route('/guest/recipes', methods=['GET'])
def api_get_public_recipes():
    """
    Get public recipes for guests
    ---
    tags:
      - Guest
    responses:
      200:
        description: List of public recipes
    """
    return get_public_recipes()

@api_bp.route('/guest/recipes/<int:recipe_id>', methods=['GET'])
def api_get_recipe_details(recipe_id):
    """
    Get recipe details
    ---
    tags:
      - Guest
    parameters:
      - name: recipe_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Recipe details
      404:
        description: Recipe not found
    """
    return get_recipe_details(recipe_id)

@api_bp.route('/guest/recipes/search', methods=['GET'])
def api_search_recipes():
    """
    Search recipes by name or ingredients
    ---
    tags:
      - Guest
    parameters:
      - name: q
        in: query
        type: string
        required: true
        description: Search query
    responses:
      200:
        description: Search results
    """
    return search_recipes()

@api_bp.route('/guest/ingredients', methods=['GET'])
def api_get_ingredients():
    """
    Get available ingredients
    ---
    tags:
      - Guest
    responses:
      200:
        description: List of ingredients
    """
    return get_ingredients()

@api_bp.route('/guest/categories', methods=['GET'])
def api_get_recipe_categories():
    """
    Get recipe categories
    ---
    tags:
      - Guest
    responses:
      200:
        description: List of categories
    """
    return get_recipe_categories()

# ==================== AUTHENTICATION ROUTES ====================

@api_bp.route('/auth/register', methods=['POST'])
@require_json
def api_register():
    """
    User registration
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
            - email
          properties:
            username:
              type: string
              example: user123
            password:
              type: string
              example: pass123
            email:
              type: string
              example: user@example.com
            family_size:
              type: integer
              example: 4
            dietary_preferences:
              type: array
              items:
                type: string
              example: ["vegetarian", "low_carb"]
            budget:
              type: number
              example: 1000000
    responses:
      201:
        description: User registered successfully
      400:
        description: Invalid input
    """
    return register()

@api_bp.route('/auth/login', methods=['POST'])
@require_json
def api_login():
    """
    User login
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: user123
            password:
              type: string
              example: pass123
    responses:
      200:
        description: Login successful
      401:
        description: Invalid credentials
    """
    return login()

# ==================== USER ROUTES (Người dùng) ====================

@api_bp.route('/user/profile', methods=['GET'])
@require_auth
def api_get_user_profile():
    """
    Get user profile
    ---
    tags:
      - User
    security:
      - BearerAuth: []
    responses:
      200:
        description: User profile
    """
    # Extract user_id from token (simplified)
    user_id = 1  # In real app, extract from JWT token
    return get_user_profile(user_id)

@api_bp.route('/user/profile', methods=['PUT'])
@require_json
@require_auth
def api_update_user_profile():
    """
    Update user profile
    ---
    tags:
      - User
    security:
      - BearerAuth: []
    responses:
      200:
        description: Profile updated
    """
    user_id = 1  # In real app, extract from JWT token
    return update_user_profile(user_id)

@api_bp.route('/user/meal-plans', methods=['POST'])
@require_json
@require_auth
def api_create_meal_plan():
    """
    Create new meal plan
    ---
    tags:
      - User
    security:
      - BearerAuth: []
    responses:
      201:
        description: Meal plan created
    """
    user_id = 1  # In real app, extract from JWT token
    return create_meal_plan(user_id)

@api_bp.route('/user/meal-plans', methods=['GET'])
@require_auth
def api_get_user_meal_plans():
    """
    Get user's meal plans
    ---
    tags:
      - User
    security:
      - BearerAuth: []
    responses:
      200:
        description: List of meal plans
    """
    user_id = 1  # In real app, extract from JWT token
    return get_user_meal_plans(user_id)

@api_bp.route('/user/meals/<int:meal_id>/recipes', methods=['POST'])
@require_json
@require_auth
def api_add_recipe_to_meal(meal_id):
    """
    Add recipe to meal
    ---
    tags:
      - User
    security:
      - BearerAuth: []
    responses:
      201:
        description: Recipe added to meal
    """
    user_id = 1  # In real app, extract from JWT token
    return add_recipe_to_meal(user_id, meal_id)

# ==================== ADMIN ROUTES (Quản trị viên) ====================

@api_bp.route('/admin/users', methods=['GET'])
@require_auth
@require_role('admin')
def api_get_all_users():
    """
    Get all users (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: List of all users
    """
    return get_all_users()

@api_bp.route('/admin/users/<int:user_id>', methods=['GET'])
@require_auth
@require_role('admin')
def api_get_user_by_id(user_id):
    """
    Get user by ID (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: User details
    """
    return get_user_by_id(user_id)

@api_bp.route('/admin/users/<int:user_id>/role', methods=['PUT'])
@require_json
@require_auth
@require_role('admin')
def api_update_user_role(user_id):
    """
    Update user role (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: User role updated
    """
    return update_user_role(user_id)

@api_bp.route('/admin/users/<int:user_id>', methods=['DELETE'])
@require_auth
@require_role('admin')
def api_delete_user(user_id):
    """
    Delete user (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: User deleted
    """
    return delete_user(user_id)

@api_bp.route('/admin/recipes', methods=['GET'])
@require_auth
@require_role('admin')
def api_get_all_recipes():
    """
    Get all recipes (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: List of all recipes
    """
    return get_all_recipes()

@api_bp.route('/admin/recipes/<int:recipe_id>/approve', methods=['PUT'])
@require_auth
@require_role('admin')
def api_approve_recipe(recipe_id):
    """
    Approve recipe (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: Recipe approved
    """
    return approve_recipe(recipe_id)

@api_bp.route('/admin/recipes/<int:recipe_id>/reject', methods=['PUT'])
@require_auth
@require_role('admin')
def api_reject_recipe(recipe_id):
    """
    Reject recipe (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: Recipe rejected
    """
    return reject_recipe(recipe_id)

@api_bp.route('/admin/recipes/<int:recipe_id>', methods=['DELETE'])
@require_auth
@require_role('admin')
def api_delete_recipe(recipe_id):
    """
    Delete recipe (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: Recipe deleted
    """
    return delete_recipe(recipe_id)

@api_bp.route('/admin/ingredients', methods=['GET'])
@require_auth
@require_role('admin')
def api_get_all_ingredients():
    """
    Get all ingredients (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: List of all ingredients
    """
    return get_all_ingredients()

@api_bp.route('/admin/ingredients', methods=['POST'])
@require_json
@require_auth
@require_role('admin')
def api_add_ingredient():
    """
    Add new ingredient (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      201:
        description: Ingredient added
    """
    return add_ingredient()

@api_bp.route('/admin/stats', methods=['GET'])
@require_auth
@require_role('admin')
def api_get_system_stats():
    """
    Get system statistics (Admin only)
    ---
    tags:
      - Admin
    security:
      - BearerAuth: []
    responses:
      200:
        description: System statistics
    """
    return get_system_stats()

# ==================== NUTRITIONIST ROUTES (Chuyên gia dinh dưỡng) ====================

@api_bp.route('/nutritionist/meal-plans/<int:meal_plan_id>/analyze', methods=['GET'])
@require_auth
@require_role('nutritionist')
def api_analyze_meal_plan_nutrition(meal_plan_id):
    """
    Analyze meal plan nutrition
    ---
    tags:
      - Nutritionist
    security:
      - BearerAuth: []
    responses:
      200:
        description: Nutrition analysis
    """
    return analyze_meal_plan_nutrition(meal_plan_id)

@api_bp.route('/nutritionist/recipes/<int:recipe_id>/suggestions', methods=['GET'])
@require_auth
@require_role('nutritionist')
def api_suggest_recipe_improvements(recipe_id):
    """
    Suggest recipe improvements
    ---
    tags:
      - Nutritionist
    security:
      - BearerAuth: []
    responses:
      200:
        description: Recipe suggestions
    """
    return suggest_recipe_improvements(recipe_id)

@api_bp.route('/nutritionist/users/<int:user_id>/nutrition-plan', methods=['POST'])
@require_json
@require_auth
@require_role('nutritionist')
def api_create_nutrition_plan(user_id):
    """
    Create nutrition plan for user
    ---
    tags:
      - Nutritionist
    security:
      - BearerAuth: []
    responses:
      201:
        description: Nutrition plan created
    """
    return create_nutrition_plan(user_id)

@api_bp.route('/nutritionist/recommendations', methods=['GET'])
@require_auth
@require_role('nutritionist')
def api_get_nutrition_recommendations():
    """
    Get nutrition recommendations
    ---
    tags:
      - Nutritionist
    security:
      - BearerAuth: []
    responses:
      200:
        description: Nutrition recommendations
    """
    return get_nutrition_recommendations()

# ==================== PLANNER ROUTES (Người lập kế hoạch) ====================

@api_bp.route('/planner/weekly-meal-plans', methods=['POST'])
@require_json
@require_auth
@require_role('planner')
def api_create_weekly_meal_plan():
    """
    Create weekly meal plan
    ---
    tags:
      - Planner
    security:
      - BearerAuth: []
    responses:
      201:
        description: Weekly meal plan created
    """
    user_id = 1  # In real app, extract from JWT token
    return create_weekly_meal_plan(user_id)

@api_bp.route('/planner/meals/<int:meal_id>/suggestions', methods=['GET'])
@require_auth
@require_role('planner')
def api_suggest_recipes_for_meal(meal_id):
    """
    Suggest recipes for meal
    ---
    tags:
      - Planner
    security:
      - BearerAuth: []
    responses:
      200:
        description: Recipe suggestions
    """
    return suggest_recipes_for_meal(meal_id)

@api_bp.route('/planner/meal-plans/<int:meal_plan_id>/shopping-list', methods=['POST'])
@require_auth
@require_role('planner')
def api_generate_shopping_list(meal_plan_id):
    """
    Generate shopping list from meal plan
    ---
    tags:
      - Planner
    security:
      - BearerAuth: []
    responses:
      201:
        description: Shopping list generated
    """
    return generate_shopping_list(meal_plan_id)

@api_bp.route('/planner/meal-plans/<int:meal_plan_id>/optimize', methods=['GET'])
@require_auth
@require_role('planner')
def api_optimize_meal_plan(meal_plan_id):
    """
    Optimize meal plan
    ---
    tags:
      - Planner
    security:
      - BearerAuth: []
    responses:
      200:
        description: Meal plan optimization
    """
    return optimize_meal_plan(meal_plan_id)

@api_bp.route('/planner/meal-plans/<int:meal_plan_id>/share', methods=['POST'])
@require_json
@require_auth
@require_role('planner')
def api_share_meal_plan(meal_plan_id):
    """
    Share meal plan with other users
    ---
    tags:
      - Planner
    security:
      - BearerAuth: []
    responses:
      201:
        description: Meal plan shared
    """
    return share_meal_plan(meal_plan_id)

@api_bp.route('/favicon.ico', methods=['GET'])
def favicon():
    """
    Favicon endpoint
    ---
    tags:
      - General
    responses:
      204:
        description: No content
    """
    return '', 204