from mobile.utils import clear, pause, delay_print
from mobile.api.api_client import get_recipes

def menu_screen(user):
    while True:
        clear()
        print("╔══════════════════════════╗")
        print("║      🍽️ THỰC ĐƠN HÔM NAY  ║")
        print("╚══════════════════════════╝")

        try:
            recipes = get_recipes()
            if not recipes:
                print("⚠️ Hiện chưa có món nào trong hệ thống.")
            else:
                for r in recipes:
                    print(f"[{r['id']}] 🍲 {r['title']}\n   📖 {r['detail'][:50]}...\n")
        except Exception as e:
            delay_print(f"❌ Lỗi tải thực đơn: {e}")

        print("\n0. ⬅️ Quay lại")
        choice = input("👉 Nhập ID món để xem chi tiết: ")
        if choice == "0":
            break
        else:
            delay_print(f"\n👉 Bạn đã chọn món #{choice}")
            pause()
