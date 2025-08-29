from mobile.utils import clear, pause, delay_print
from mobile.api.api_client import login

def login_screen():
    clear()
    print("╔══════════════════════════╗")
    print("║        🔐 ĐĂNG NHẬP       ║")
    print("╚══════════════════════════╝")
    username = input("👤 Tên đăng nhập: ")
    password = input("🔑 Mật khẩu: ")

    try:
        result = login(username, password)
        delay_print(f"\n✅ Đăng nhập thành công! Xin chào {result['fullname']} 👋")
        pause()
        return result
    except Exception as e:
        delay_print(f"\n❌ Lỗi đăng nhập: {e}")
        pause()
        return None
