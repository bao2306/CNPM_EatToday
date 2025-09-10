from functools import wraps
from flask import request, jsonify
from src.infrastructure.model import User
from src.infrastructure.database.base import db

def require_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
        return f(*args, **kwargs)
    return decorated_function

def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Missing or invalid Authorization header. Expected: Bearer <token>"}), 401
        
        token = auth_header.split(' ')[1]
        
        # Trong thực tế, decode JWT token để lấy user_id
        # Ở đây chúng ta giả lập bằng cách tìm user đầu tiên
        user = User.query.first()
        if not user:
            return jsonify({"error": "User not found"}), 401
        
        # Lưu user vào request context để sử dụng trong controller
        request.current_user = user
        return f(*args, **kwargs)
    return decorated_function

def require_role(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Kiểm tra authentication trước
            if not hasattr(request, 'current_user') or not request.current_user:
                return jsonify({"error": "Authentication required"}), 401
            
            user = request.current_user
            
            # Kiểm tra role
            if user.role != required_role:
                return jsonify({
                    "error": f"Access denied. Required role: {required_role}, Current role: {user.role}"
                }), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator