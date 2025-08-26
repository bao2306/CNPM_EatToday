from screens.login import login_screen
from screens.profile import profile_screen
from screens.menu import menu_screen
from screens.recipe import recipe_screen
from screens.history import history_screen

def main():
    print("===== Ứng dụng EatToday (CLI) =====")
    user_id = None

    while not user_id:
        user_id = login_screen()

    while True:
        print("\n--- MENU CHÍNH ---")
        print("1. Xem hồ sơ")
        print("2. Gợi ý thực đơn")
        print("3. Xem công thức món ăn")
        print("4. Lịch sử món đã ăn")
        print("0. Thoát")

        choice = input("👉 Chọn chức năng: ").strip()
        if choice == "1":
            profile_screen(user_id)
        elif choice == "2":
            menu_screen()
        elif choice == "3":
            recipe_screen()
        elif choice == "4":
            history_screen(user_id)
        elif choice == "0":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
