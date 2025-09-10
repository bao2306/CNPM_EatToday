from flasgger import Swagger

def init_swagger(app):
    swagger_config = {
        "title": "Eat Today API",
        "version": "1.0",
        "description": "API documentation for Eat Today application",
        "termsOfService": "http://example.com/terms/",
        "contact": {"email": "contact@example.com"},
        "schemes": ["http", "https"],
        "swagger": "2.0",
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: rule.rule.startswith('/api') and rule.rule != '/api/favicon.ico',
                "model_filter": lambda tag: True,
            }
        ],
        "headers": [],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
        "securityDefinitions": {
            "BearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Enter: Bearer fake-jwt-token"
            }
        }
    }
    Swagger(app, config=swagger_config)
    print("Swagger initialized successfully")