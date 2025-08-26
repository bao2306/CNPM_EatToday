import asyncio
from mobile.api import login

async def login_screen():
    print("=== Đăng nhập ===")
    username = input("Nhập username: ")
    password = input("Nhập password: ")

    result = await login(username, password)
    print("👉 Kết quả đăng nhập:", result)

if __name__ == "__main__":
    asyncio.run(login_screen())
