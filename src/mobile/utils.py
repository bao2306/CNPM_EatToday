# mobile/utils.py
import os
import time

def clear():
    """Xoá màn hình console (Windows/Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg: str = "Nhấn Enter để tiếp tục..."):
    """Dừng màn hình chờ người dùng nhấn Enter."""
    input(msg)

def delay_print(msg: str, delay: float = 0.02):
    """In chữ từng ký tự (tạo cảm giác loading)."""
    for ch in msg:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()
