from flask import jsonify, request
from src.domain.model import User

def login():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400
    user = User(id=1, username=data.get('username'), password_hash="hashed_pass")
    if data.get('username') == 'user' and data.get('password') == 'pass':
        return jsonify({"token": "fake-jwt-token", "message": "Login successful", "user": user.__dict__})
    return jsonify({"error": "Invalid credentials"}), 401

def register():
    data = request.json
    if not data or 'username' not in data:
        return jsonify({"error": "Missing username"}), 400
    user = User(id=1, username=data.get('username'), password_hash="hashed_pass")
    return jsonify({"message": f"User {user.username} registered", "user": user.__dict__})