# Architecture


eat-today-api/
    ├── doc
    │   └── Cấu trúc chủ đề Eat Today
    ├── src
    │   ├── api
    │   │   ├── controllers
    │   │   │   └── ...  
    │   │   ├── schemas
    │   │   │   └── ...  
    │   │   ├── middleware.py
    │   │   ├── responses.py
    │   │   └── requests.py
    │   ├── infrastructure
    │   │   ├── services
    │   │   │   └── ... 
    │   │   ├── databases
    │   │   │   └── ...  
    │   │   ├── repositories
    │   │   │   └── ...  
    │   │   └── models
    │   │   │   └── ...  
    │   ├── domain
    │   │   ├── constants.py
    │   │   ├── exceptions.py
    │   │   ├── models
    │   │   │   └── ...  # Business logic models
    │   ├── services
    │   │    └── ... 
    │   ├── app.py
    │   ├── config.py
    │   ├── cors.py
    │   ├── create_app.py
    │   ├── dependency_container.py
    │   ├── error_handler.py
    │   └── logging.py