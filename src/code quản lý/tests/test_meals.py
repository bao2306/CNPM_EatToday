
from .conftest import register_and_login

def test_meals_flow(client):
    headers = register_and_login(client)

   
    r = client.post("/api/v1/meals", headers=headers, json={"meal_name":"Phở bò"})
    assert r.status_code == 201

  
    r = client.get("/api/v1/meals", headers=headers)
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) >= 1

 
    r = client.get("/api/v1/suggest", headers=headers)
    assert r.status_code == 200
    assert "suggestion" in r.json()
