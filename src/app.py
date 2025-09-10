from flask import Flask, render_template
from .api import api_bp
from .cors import init_cors
from .dependency_container import init_dependency_container
from .error_handler import register_error_handlers
from .api.swagger import init_swagger 
from .infrastructure.database.init import init_db
from .infrastructure.database.base import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eat_today.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
    app.config['DEBUG'] = True  

    app.register_blueprint(api_bp, url_prefix='/api')
    init_db(app)
    init_cors(app)
    init_dependency_container(app)
    register_error_handlers(app)
    init_swagger(app)  
    
    with app.app_context():
        # Import models to register them with SQLAlchemy
        from .infrastructure.model import User, Recipe, Ingredient, MealPlan, Meal, MealRecipe, ShoppingList, ShoppingItem
        db.create_all()
        print("Database initialized successfully")  
    
    # Frontend Routes
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/login')
    def login_page():
        return render_template('login.html')
    
    @app.route('/recipes')
    def recipes_page():
        return render_template('recipes.html')
    
    @app.route('/user/dashboard')
    def user_dashboard():
        return render_template('user_dashboard.html')
    
    @app.route('/admin/dashboard')
    def admin_dashboard():
        return render_template('admin_dashboard.html')
    
    @app.route('/nutritionist/dashboard')
    def nutritionist_dashboard():
        return render_template('nutritionist_dashboard.html')
    
    @app.route('/planner/dashboard')
    def planner_dashboard():
        return render_template('planner_dashboard.html')
    
    # API Health Check
    @app.route('/health')
    def health():
        return {
            "status": "healthy",
            "database": "connected" if db.engine else "disconnected"
        }
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)