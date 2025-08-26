# main.py
from sceens.login import login_screen
from sceens.profile import profile_screen
from sceens.menu import menu_screen
from sceens.recipe import recipe_screen
from sceens.history import history_screen

def main():
    print("===== Ứng dụng EatToday =====")
    user_id = None

    # Đăng nhập trước
    while not user_id:
        user_id = login_screen()

    # Menu chính
    while True:
        print("\n--- MENU CHÍNH ---")
        print("1. Xem hồ sơ")
        print("2. Gợi ý thực đơn")
        print("3. Xem công thức món ăn")
        print("4. Lịch sử món đã ăn")
        print("0. Thoát")

        choice = input("👉 Chọn chức năng: ")

        if choice == "1":
            profile_screen(user_id)
        elif choice == "2":
            menu_screen()
        elif choice == "3":
            recipe_screen()
        elif choice == "4":
            history_screen(user_id)
        elif choice == "0":
            print("👋 Tạm biệt, hẹn gặp lại!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
