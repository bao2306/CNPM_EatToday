# api.py
import requests

BASE_URL = "http://127.0.0.1:8000"   # đổi thành URL backend thật

def login_api(username, password):
    response = requests.post(f"{BASE_URL}/login", json={
        "username": username,
        "password": password
    })
    return response.json()

def get_profile(user_id):
    response = requests.get(f"{BASE_URL}/profile/{user_id}")
    return response.json()

def get_menu(menu_type="daily"):
    response = requests.get(f"{BASE_URL}/menu?type={menu_type}")
    return response.json()

def get_recipe(recipe_id):
    response = requests.get(f"{BASE_URL}/recipe/{recipe_id}")
    return response.json()

def get_history(user_id):
    response = requests.get(f"{BASE_URL}/history/{user_id}")
    return response.json()
