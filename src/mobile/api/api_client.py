import requests
from mobile.config import BASE_URL
from mobile.services.session_manager import load_session

def request_api(method: str, endpoint: str, data: dict = None):
    url = f"{BASE_URL}{endpoint}"
    headers = {}
    session = load_session()
    if "token" in session:
        headers["Authorization"] = f"Bearer {session['token']}"
    try:
        if method == "GET":
            res = requests.get(url, headers=headers)
        else:
            res = requests.post(url, json=data, headers=headers)
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def signup(username: str, password: str, fullname: str = "") -> dict:
    return request_api("POST", "/signup", {"username": username, "password": password, "fullname": fullname})

def login(username: str, password: str) -> dict:
    return request_api("POST", "/login", {"username": username, "password": password})

def get_recipes() -> dict:
    return request_api("GET", "/recipes")

def get_profile(user_id: int) -> dict:
    return request_api("GET", f"/profile/{user_id}")

def get_history(user_id: int) -> dict:
    return request_api("GET", f"/history/{user_id}")
