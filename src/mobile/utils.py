import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    """Xoá màn hình console (Windows/Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg: str = f"{Fore.CYAN}👉 Nhấn Enter để tiếp tục...{Style.RESET_ALL}"):
    """Dừng màn hình chờ người dùng nhấn Enter."""
    input(msg)

def delay_print(msg: str, delay: float = 0.02, color: str = Fore.WHITE):
    """In chữ từng ký tự với màu sắc (tạo cảm giác loading)."""
    for ch in msg:
        print(color + ch + Style.RESET_ALL, end="", flush=True)
        time.sleep(delay)
    print()

def success(msg: str):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")

def error(msg: str):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")

def warning(msg: str):
    print(f"{Fore.YELLOW}⚠️ {msg}{Style.RESET_ALL}")

def info(msg: str):
    print(f"{Fore.CYAN}ℹ️ {msg}{Style.RESET_ALL}")
