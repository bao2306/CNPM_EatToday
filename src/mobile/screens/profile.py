from mobile.utils import clear, pause, delay_print
from mobile.api.api_client import get_profile

def profile_screen(user):
    clear()
    print("╔══════════════════════════╗")
    print("║     👤 HỒ SƠ CÁ NHÂN      ║")
    print("╚══════════════════════════╝")

    try:
        profile = get_profile(user["user_id"])
        print(f"🆔 ID: {profile['id']}")
        print(f"👤 Username: {profile['username']}")
        print(f"📛 Họ tên: {profile['fullname']}")
    except Exception as e:
        delay_print(f"❌ Lỗi tải hồ sơ: {e}")
    pause()
