from screens.api import get_history

def history_screen(user_id):
    res = get_history(user_id)
    if res["success"]:
        meals = res["data"].get("meals") if isinstance(res["data"], dict) else res["data"]
        print("\n===== Lịch sử món đã chọn =====")
        if meals:
            for idx, meal in enumerate(meals, start=1):
                print(f"{idx}. {meal}")
        else:
            print("Chưa có lịch sử.")
        print("================================\n")
    else:
        print("❌ Lấy lịch sử thất bại:", res["error"] or res["data"])

