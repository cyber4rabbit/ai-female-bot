from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat():
    payload = {
        "user_id": "student01",
        "question": "Sprawdź zgłoszenie INC1001 i zadania w Jira"
    }
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "bot_name" in data
    assert "answer" in data
    assert "sources" in data