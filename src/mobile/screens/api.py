
import requests

BASE_URL = "http://127.0.0.1:8000"   
TIMEOUT = 5 

def _handle_response(resp):
    try:
        data = resp.json()
    except ValueError:
        data = resp.text
    return {
        "success": resp.ok,
        "status": resp.status_code,
        "data": data,
        "error": None if resp.ok else data
    }

def login_api(username, password):
    try:
        resp = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password}, timeout=TIMEOUT)
        return _handle_response(resp)
    except requests.RequestException as e:
        return {"success": False, "status": None, "data": None, "error": str(e)}

def get_profile(user_id):
    try:
        resp = requests.get(f"{BASE_URL}/profile/{user_id}", timeout=TIMEOUT)
        return _handle_response(resp)
    except requests.RequestException as e:
        return {"success": False, "status": None, "data": None, "error": str(e)}

def get_menu(menu_type="daily"):
    try:
        resp = requests.get(f"{BASE_URL}/menu", params={"type": menu_type}, timeout=TIMEOUT)
        return _handle_response(resp)
    except requests.RequestException as e:
        return {"success": False, "status": None, "data": None, "error": str(e)}

def get_recipe(recipe_id):
    try:
        resp = requests.get(f"{BASE_URL}/recipe/{recipe_id}", timeout=TIMEOUT)
        return _handle_response(resp)
    except requests.RequestException as e:
        return {"success": False, "status": None, "data": None, "error": str(e)}

def get_history(user_id):
    try:
        resp = requests.get(f"{BASE_URL}/history/{user_id}", timeout=TIMEOUT)
        return _handle_response(resp)
    except requests.RequestException as e:
        return {"success": False, "status": None, "data": None, "error": str(e)}
