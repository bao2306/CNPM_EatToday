from mobile.utils import clear, pause, delay_print
from mobile.api.api_client import get_history

def history_screen(user):
    clear()
    print("╔══════════════════════════╗")
    print("║      📜 LỊCH SỬ MÓN ĂN    ║")
    print("╚══════════════════════════╝")

    try:
        history = get_history(user["user_id"])
        if not history:
            delay_print("⚠️ Bạn chưa có lịch sử món ăn nào.")
        else:
            for item in history:
                print(f"- 🍴 Món #{item['recipe_id']}")
    except Exception as e:
        delay_print(f"❌ Lỗi tải lịch sử: {e}")
    pause()
