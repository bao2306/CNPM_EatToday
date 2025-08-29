from mobile.utils import clear, pause, delay_print

def recipe_screen(recipe):
    clear()
    print("╔══════════════════════════╗")
    print("║     📖 CHI TIẾT MÓN ĂN    ║")
    print("╚══════════════════════════╝")
    print(f"\n🍲 {recipe['title']}")
    print(f"\n📝 Mô tả: {recipe['detail']}")
    pause()
