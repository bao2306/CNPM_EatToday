from flask import jsonify

def default_route():
    return jsonify({"message": "Welcome to Eat Today API"})