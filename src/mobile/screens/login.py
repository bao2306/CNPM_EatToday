from screens.api import login_api

def login_screen():
    print("=== Đăng nhập ===")
    username = input("👤 Tên đăng nhập: ").strip()
    password = input("🔑 Mật khẩu: ").strip()

    res = login_api(username, password)
    if res["success"]:
        # backend nên trả user info hoặc user_id
        user = res["data"]
        user_id = user.get("user_id") or user.get("id")
        print("✅ Đăng nhập thành công!")
        return user_id
    else:
        print("❌ Đăng nhập thất bại:", res["error"] or res["data"])
        return None

if __name__ == "__main__":
    login_screen()
