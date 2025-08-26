# recipe.py
from sceens.api import get_recipe

def recipe_screen():
    recipe_id = input("Nhập ID món ăn cần xem chi tiết: ")
    recipe = get_recipe(recipe_id)

    print(f"\n===== Công thức: {recipe.get('name')} =====")
    print("Nguyên liệu:")
    for ing in recipe.get("ingredients", []):
        print(f"- {ing}")
    print("\nCách nấu:")
    print(recipe.get("instructions"))
    print("==========================================\n")
