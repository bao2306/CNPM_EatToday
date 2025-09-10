from .app import create_app as base_create_app
from .cors import init_cors
from .dependency_container import init_dependency_container

def create_app():
    app = base_create_app()
    init_cors(app)
    init_dependency_container(app)
    return app