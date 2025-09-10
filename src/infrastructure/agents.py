class UserAgent:
    def get_menu(self):
        return {"menu": ["Lẩu kè hoạch bữa ăn", "Quản lý thông tin cá nhân", "Quản lý ngân sách"]}

    def get_profile(self):
        return {"name": "User", "budget": 100}

class GuestAgent:
    def get_recipes(self):
        return {"recipes": ["Xem công thức", "Tìm kiếm công thức", "Xem chi tiết công thức"]}

class NutritionExpertAgent:
    def create_nutrition_plan(self, data):
        return {"plan": f"Nutrition plan for {data.get('user')}", "dishes": ["Thực đơn dinh dưỡng", "Đánh giá món ăn"]}

class PlannerAgent:
    def create_schedule(self, data):
        return {"schedule": f"Schedule for {data.get('date')}", "tasks": ["Tạo kế hoạch chi tiết", "Quản lý lịch"]}

class AdminAgent:
    def manage_system(self, data):
        return {"status": "managed", "actions": ["Quản lý tài khoản", "Quản lý thông tin"]}