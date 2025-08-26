import asyncio
from mobile.api import get_profile

async def profile_screen():
    print("=== Hồ sơ cá nhân ===")
    user_id = int(input("Nhập user_id: "))

    result = await get_profile(user_id)
    print("👉 Hồ sơ:", result)

if __name__ == "__main__":
    asyncio.run(profile_screen())
