import builtins
import pytest
from screens import login, menu

def test_login_screen_success(monkeypatch, capsys):
    # giả lập input username, password
    inputs = iter(["alice", "secret"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))
    # giả lập api
    monkeypatch.setattr("screens.login.login_api", lambda u,p: {"success": True, "data": {"user_id": 5}})
    uid = login.login_screen()
    captured = capsys.readouterr()
    assert uid == 5
    assert "Đăng nhập thành công" in captured.out

def test_menu_screen_shows_items(monkeypatch, capsys):
    # giả lập input menu type
    monkeypatch.setattr(builtins, "input", lambda prompt="": "daily")
    monkeypatch.setattr("screens.menu.get_menu", lambda t="daily": {"success": True, "data": {"meals": ["Pho", "Banh Mi"]}})
    menu.menu_screen()
    out = capsys.readouterr().out
    assert "1. Pho" in out
    assert "2. Banh Mi" in out
