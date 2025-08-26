# profile.py
from sceens.api import get_profile

def profile_screen(user_id):
    profile = get_profile(user_id)
    print("\n===== Hồ sơ cá nhân =====")
    print(f"👤 Tên: {profile.get('name')}")
    print(f"📧 Email: {profile.get('email')}")
    print(f"🍳 Sở thích: {profile.get('preferences')}")
    print("=========================\n")
