from screens.api import get_recipe

def recipe_screen():
    recipe_id = input("Nhập ID món ăn cần xem chi tiết: ").strip()
    if not recipe_id:
        print("❌ Bạn chưa nhập ID.")
        return
    res = get_recipe(recipe_id)
    if res["success"]:
        r = res["data"]
        print(f"\n===== Công thức: {r.get('name')} =====")
        print("Nguyên liệu:")
        for ing in r.get("ingredients", []):
            print(f"- {ing}")
        print("\nCách nấu:")
        print(r.get("instructions", "Không có hướng dẫn."))
        print("==========================================\n")
    else:
        print("❌ Lấy công thức thất bại:", res["error"] or res["data"])
