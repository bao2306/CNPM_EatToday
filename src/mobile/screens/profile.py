from screens.api import get_profile

def profile_screen(user_id):
    res = get_profile(user_id)
    if res["success"]:
        p = res["data"]
        print("\n===== Hồ sơ cá nhân =====")
        print(f"👤 Tên: {p.get('name')}")
        print(f"📧 Email: {p.get('email')}")
        print(f"🍳 Sở thích: {p.get('preferences')}")
        print("=========================\n")
    else:
        print("❌ Không thể lấy hồ sơ:", res["error"] or res["data"])
