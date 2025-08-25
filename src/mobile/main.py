from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


# ---------------- Các màn hình ----------------
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Label(text="🍽️ Hôm nay ăn gì?", font_size=32))
        layout.add_widget(Button(text="Đăng nhập / Đăng ký", on_press=self.goto_login))
        layout.add_widget(Button(text="Hồ sơ cá nhân", on_press=self.goto_profile))
        layout.add_widget(Button(text="Gợi ý thực đơn", on_press=self.goto_menu))
        layout.add_widget(Button(text="Công thức nấu ăn", on_press=self.goto_recipe))
        layout.add_widget(Button(text="Lịch sử món ăn", on_press=self.goto_history))

        self.add_widget(layout)

    def goto_login(self, instance):
        self.manager.current = "login"

    def goto_profile(self, instance):
        self.manager.current = "profile"

    def goto_menu(self, instance):
        self.manager.current = "menu"

    def goto_recipe(self, instance):
        self.manager.current = "recipe"

    def goto_history(self, instance):
        self.manager.current = "history"


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="🔑 Đây là màn hình Login/Signup"))


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="👤 Đây là màn hình Hồ sơ cá nhân"))


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="📅 Đây là màn hình Gợi ý thực đơn"))


class RecipeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="🍳 Đây là màn hình Công thức nấu ăn"))


class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="📖 Đây là màn hình Lịch sử món ăn"))


# ---------------- App chính ----------------
class EatTodayApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(RecipeScreen(name="recipe"))
        sm.add_widget(HistoryScreen(name="history"))
        return sm


if __name__ == "__main__":
    EatTodayApp().run()
