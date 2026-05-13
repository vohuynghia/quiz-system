import pytest
import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# 1
def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json() == {"ok": True}

# 2
def test_get_questions():
    r = client.get("/api/questions/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

# 3
def test_create_question():
    r = client.post("/api/questions/", json={
        "content": "Test question?",
        "options": json.dumps(["A", "B", "C", "D"]),
        "correct_answer": "A",
        "category": "test"
    })
    assert r.status_code == 200
    assert r.json()["content"] == "Test question?"

# 4
def test_get_question_by_id():
    r = client.get("/api/questions/1")
    assert r.status_code == 200
    assert "content" in r.json()

# 5
def test_get_question_not_found():
    r = client.get("/api/questions/99999")
    assert r.status_code == 404

# 6
def test_get_quizzes():
    r = client.get("/api/quizzes/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

# 7
def test_create_quiz():
    r = client.post("/api/quizzes/", json={
        "title": "Test Quiz",
        "description": "Quiz for testing"
    })
    assert r.status_code == 200
    assert r.json()["title"] == "Test Quiz"

# 8
def test_get_results():
    r = client.get("/api/results/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

# 9
def test_submit_quiz():
    r = client.post("/api/results/submit", json={
        "quiz_id": 1,
        "answers": [
            {"question_id": 1, "selected_option": "Not Found"},
            {"question_id": 2, "selected_option": "Containerize ứng dụng"}
        ]
    })
    assert r.status_code == 200
    assert "score" in r.json()

# 10
def test_submit_quiz_score_correct():
    r = client.post("/api/results/submit", json={
        "quiz_id": 1,
        "answers": [
            {"question_id": 1, "selected_option": "Not Found"}
        ]
    })
    assert r.json()["score"] == 100.0

# 11
def test_submit_quiz_score_wrong():
    r = client.post("/api/results/submit", json={
        "quiz_id": 1,
        "answers": [
            {"question_id": 1, "selected_option": "Wrong Answer"}
        ]
    })
    assert r.json()["score"] == 0.0

# 12
def test_auth_ping():
    r = client.get("/api/auth/ping")
    assert r.status_code == 200
    assert r.json()["message"] == "auth router OK"

# 13
def test_question_has_required_fields():
    r = client.get("/api/questions/1")
    data = r.json()
    assert "content" in data
    assert "options" in data
    assert "correct_answer" in data
    assert "category" in data