# history.py
from sceens.api import get_history

def history_screen(user_id):
    history = get_history(user_id)
    print("\n===== Lịch sử món đã chọn =====")
    for idx, meal in enumerate(history.get("meals", []), start=1):
        print(f"{idx}. {meal}")
    print("================================\n")
