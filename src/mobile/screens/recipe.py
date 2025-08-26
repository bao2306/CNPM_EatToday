import asyncio
from mobile.api import get_recipe

async def recipe_screen():
    print("=== Trang chi tiết công thức ===")
    recipe_id = int(input("Nhập ID món ăn: "))

    result = await get_recipe(recipe_id)
    print("👉 Công thức món ăn:", result)

if __name__ == "__main__":
    asyncio.run(recipe_screen())
