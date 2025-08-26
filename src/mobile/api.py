import httpx

BASE_URL = "http://127.0.0.1:8000"  # URL backend FastAPI

# Đăng nhập
async def login(username: str, password: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/login", json={
            "username": username,
            "password": password
        })
        return response.json()

# Hồ sơ cá nhân
async def get_profile(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/profile/{user_id}")
        return response.json()

# Thực đơn
async def get_menu():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/menu")
        return response.json()

# Chi tiết công thức
async def get_recipe(recipe_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/recipe/{recipe_id}")
        return response.json()

# Lịch sử
async def get_history(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/history/{user_id}")
        return response.json()
