# menu.py
from sceens.api import get_menu

def menu_screen():
    choice = input("Bạn muốn xem thực đơn (daily/weekly): ")
    menu = get_menu(choice)

    print(f"\n===== Gợi ý thực đơn ({choice}) =====")
    for idx, item in enumerate(menu.get("meals", []), start=1):
        print(f"{idx}. {item}")
    print("=====================================\n")
