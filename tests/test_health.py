from fastapi.testclient import TestClient
from sugarvany_api.interface.api.app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "pong"} 