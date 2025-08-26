import asyncio
from mobile.api import get_menu

async def menu_screen():
    print("=== Trang gợi ý thực đơn ===")
    result = await get_menu()

    print("👉 Thực đơn hôm nay:")
    for item in result:
        print(f"- {item}")

if __name__ == "__main__":
    asyncio.run(menu_screen())
