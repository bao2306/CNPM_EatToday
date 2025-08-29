from mobile.utils import clear, pause, delay_print
from mobile.screens.login_screen import login_screen
from mobile.screens.signup_screen import signup_screen
from mobile.screens.menu_screen import menu_screen
from mobile.screens.profile_screen import profile_screen
from mobile.screens.history_screen import history_screen


def main_menu(user):
    """Menu chính sau khi đăng nhập"""
    while True:
        clear()
        print("════════════════════════════════")
        print("        🍴 EAT TODAY APP        ")
        print("════════════════════════════════")
        print(f"Xin chào, {user['fullname']} 👋\n")

        print("1. 👤 Hồ sơ cá nhân")
        print("2. 🍽️ Thực đơn hôm nay")
        print("3. 📜 Lịch sử món ăn")
        print("0. 🚪 Đăng xuất")

        choice = input("\n👉 Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            profile_screen(user)
        elif choice == "2":
            menu_screen(user)
        elif choice == "3":
            history_screen(user)
        elif choice == "0":
            delay_print("\n🚪 Bạn đã đăng xuất. Hẹn gặp lại!")
            pause()
            break
        else:
            delay_print("⚠️ Lựa chọn không hợp lệ! Vui lòng thử lại.")
            pause()


def main():
    """Luồng chính của ứng dụng"""
    while True:
        clear()
        print("════════════════════════════════")
        print("        🎉 WELCOME TO           ")
        print("          EAT TODAY             ")
        print("════════════════════════════════")
        print("\nỨng dụng gợi ý thực đơn mỗi ngày cho gia đình bạn 🍲\n")

        print("1. 🔐 Đăng nhập")
        print("2. 📝 Đăng ký")
        print("0. ❌ Thoát")

        choice = input("\n👉 Nhập lựa chọn: ").strip()

        if choice == "1":
            user = login_screen()
            if user:
                main_menu(user)
        elif choice == "2":
            signup_screen()
        elif choice == "0":
            delay_print("\n👋 Cảm ơn bạn đã sử dụng EatToday!")
            break
        else:
            delay_print("⚠️ Lựa chọn không hợp lệ! Vui lòng thử lại.")
            pause()


if __name__ == "__main__":
    main()
