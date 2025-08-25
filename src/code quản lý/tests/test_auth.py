
def test_register_and_login(client):

    r = client.post("/api/v1/register", json={
        "username":"bob",
        "email":"bob@example.com",
        "full_name":"Bob",
        "password":"secret123"
    })
    assert r.status_code == 201

    r = client.post("/api/v1/login", data={"username":"bob","password":"secret123"})
    assert r.status_code == 200
    assert "access_token" in r.json()
