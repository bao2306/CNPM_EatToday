# login.py
from sceens.api import login_api

def login_screen():
    username = input("👤 Tên đăng nhập: ")
    password = input("🔑 Mật khẩu: ")

    result = login_api(username, password)
    if result.get("success"):
        print("✅ Đăng nhập thành công!")
        return result.get("user_id")   # trả user_id để màn khác dùng
    else:
        print("❌ Sai thông tin đăng nhập!")
        return None
