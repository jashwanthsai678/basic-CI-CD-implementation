from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_predict():
    response = client.get("/predict/4")
    assert response.json()["prediction"] == "even"