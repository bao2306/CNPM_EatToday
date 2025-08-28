from screens.api import _handle_response
import requests

BASE_URL = "http://127.0.0.1:8000"  
TIMEOUT = 5

def signup_api(username, password, fullname):
    try:
        resp = requests.post(
            f"{BASE_URL}/signup",
            json={"username": username, "password": password, "fullname": fullname},
            timeout=TIMEOUT
        )
        return _handle_response(resp)
    except requests.RequestException as e:
        return {"success": False, "status": None, "data": None, "error": str(e)}

def signup_screen():
    print("=== Đăng ký ===")
    username = input("👤 Tên đăng nhập: ").strip()
    if not username:
        print("❌ Tên đăng nhập không được để trống!")
        return None
    password = input("🔑 Mật khẩu: ").strip()
    if not password:
        print("❌ Mật khẩu không được để trống!")
        return None
    fullname = input("👤 Họ và tên: ").strip()
    if not fullname:
        print("❌ Họ và tên không được để trống!")
        return None

    res = signup_api(username, password, fullname)
    if res["success"]:
        user_id = res["data"].get("user_id")
        print("✅ Đăng ký thành công! User ID:", user_id)
        return user_id
    else:
        print("❌ Đăng ký thất bại:", res["error"] or res["data"])
        return None

if __name__ == "__main__":
    signup_screen()
