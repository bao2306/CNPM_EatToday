def init_dependency_container(app):
    app.config['agents'] = {
        'user': None,
        'guest': None,
        'nutrition_expert': None,
        'planner': None,
        'admin': None
    }