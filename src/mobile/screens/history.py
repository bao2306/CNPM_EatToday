import asyncio
from mobile.api import get_history

async def history_screen():
    print("=== Lịch sử món đã chọn ===")
    user_id = int(input("Nhập user_id: "))

    result = await get_history(user_id)
    print("👉 Lịch sử món ăn:")
    for item in result:
        print(f"- {item}")

if __name__ == "__main__":
    asyncio.run(history_screen())
