from mobile.utils import clear, pause, delay_print
from mobile.api.api_client import signup

def signup_screen():
    clear()
    print("╔══════════════════════════╗")
    print("║        📝 ĐĂNG KÝ         ║")
    print("╚══════════════════════════╝")
    username = input("👤 Tên đăng nhập: ")
    password = input("🔑 Mật khẩu: ")
    fullname = input("📛 Họ và tên: ")

    try:
        result = signup(username, password, fullname)
        delay_print("\n✅ Tạo tài khoản thành công!")
        pause()
        return result
    except Exception as e:
        delay_print(f"\n❌ Lỗi đăng ký: {e}")
        pause()
        return None
