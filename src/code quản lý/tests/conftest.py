
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import Base, engine, SessionLocal

@pytest.fixture(autouse=True, scope="session")
def setup_db():
    # Tạo bảng cho test (SQLite file)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def client():
    return TestClient(app)

def register_and_login(client):
    client.post("/api/v1/register", json={
        "username":"alice",
        "email":"alice@example.com",
        "full_name":"Alice",
        "password":"secret123"
    })
    r = client.post("/api/v1/login", data={"username":"alice","password":"secret123"})
    token = r.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
