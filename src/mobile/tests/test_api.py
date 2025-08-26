import requests
import pytest
from screens import api

class MockResp:
    def __init__(self, status, data):
        self.status_code = status
        self._data = data
    @property
    def ok(self):
        return 200 <= self.status_code < 300
    def json(self):
        return self._data
    @property
    def text(self):
        return str(self._data)

def test_login_success(monkeypatch):
    def fake_post(url, json, timeout):
        return MockResp(200, {"user_id": 42, "username": json["username"]})
    monkeypatch.setattr(requests, "post", fake_post)
    res = api.login_api("u","p")
    assert res["success"] is True
    assert res["data"]["user_id"] == 42

def test_login_fail(monkeypatch):
    def fake_post(url, json, timeout):
        return MockResp(401, {"detail":"unauthorized"})
    monkeypatch.setattr(requests, "post", fake_post)
    res = api.login_api("u","wrong")
    assert res["success"] is False
    assert res["status"] == 401

def test_get_recipe_notfound(monkeypatch):
    def fake_get(url, timeout):
        return MockResp(404, {"detail":"not found"})
    monkeypatch.setattr(requests, "get", fake_get)
    res = api.get_recipe("999")
    assert res["success"] is False
    assert res["status"] == 404

def test_get_profile_network_error(monkeypatch):
    def fake_get(url, timeout):
        raise requests.RequestException("conn lost")
    monkeypatch.setattr(requests, "get", fake_get)
    res = api.get_profile(1)
    assert res["success"] is False
    assert "conn lost" in res["error"]
