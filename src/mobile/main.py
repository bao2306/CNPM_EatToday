from kivy.app import App
from kivy.uix.label import Label


class EatTodayApp(App):
    def build(self):
        return Label(text="Xin chào! Đây là app EatToday :)")


if __name__ == "__main__":
    EatTodayApp().run()
