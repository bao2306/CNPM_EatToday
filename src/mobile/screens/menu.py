from screens.api import get_menu

def menu_screen():
    menu_type = input("Bạn muốn xem thực đơn (daily/weekly) [daily]: ").strip() or "daily"
    res = get_menu(menu_type)
    if res["success"]:
        meals = res["data"].get("meals") if isinstance(res["data"], dict) else res["data"]
        print(f"\n===== Gợi ý thực đơn ({menu_type}) =====")
        if meals:
            for i, m in enumerate(meals, start=1):
                print(f"{i}. {m}")
        else:
            print("Không có món nào.")
        print("=====================================\n")
    else:
        print("❌ Lấy thực đơn thất bại:", res["error"] or res["data"])
