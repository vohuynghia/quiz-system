import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app.database import SessionLocal, engine
from app.models import Base, Question, Quiz

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Xóa data cũ
db.query(Question).delete()
db.query(Quiz).delete()
db.commit()

questions_data = [
    {"content": "HTTP status code 404 có nghĩa là gì?",
     "options": json.dumps(["Not Found", "Server Error", "Unauthorized", "Forbidden"]),
     "correct_answer": "Not Found", "category": "networking"},
    {"content": "Docker dùng để làm gì?",
     "options": json.dumps(["Containerize ứng dụng", "Quản lý database", "Build UI", "Test API"]),
     "correct_answer": "Containerize ứng dụng", "category": "devops"},
    {"content": "CI/CD là viết tắt của gì?",
     "options": json.dumps(["Continuous Integration/Continuous Delivery", "Code Integration/Code Delivery", "Cloud Infrastructure/Cloud Deployment", "Container Image/Container Deploy"]),
     "correct_answer": "Continuous Integration/Continuous Delivery", "category": "devops"},
    {"content": "Lệnh nào dùng để xem log container Docker?",
     "options": json.dumps(["docker logs", "docker inspect", "docker ps", "docker status"]),
     "correct_answer": "docker logs", "category": "devops"},
    {"content": "Git branch nào thường dùng cho production?",
     "options": json.dumps(["main", "dev", "feature", "hotfix"]),
     "correct_answer": "main", "category": "git"},
    {"content": "File nào KHÔNG được commit lên GitHub?",
     "options": json.dumps([".env", ".env.example", "README.md", "requirements.txt"]),
     "correct_answer": ".env", "category": "devops"},
    {"content": "FastAPI tự động tạo trang docs ở đường dẫn nào?",
     "options": json.dumps(["/docs", "/api", "/swagger", "/help"]),
     "correct_answer": "/docs", "category": "backend"},
    {"content": "SQLAlchemy là gì?",
     "options": json.dumps(["ORM cho Python", "Framework frontend", "CI/CD tool", "Container runtime"]),
     "correct_answer": "ORM cho Python", "category": "backend"},
    {"content": "CORS error xảy ra khi nào?",
     "options": json.dumps(["Frontend và backend khác origin", "Database bị lỗi", "API key sai", "Docker không chạy"]),
     "correct_answer": "Frontend và backend khác origin", "category": "networking"},
    {"content": "Lệnh nào khởi động toàn bộ services trong docker-compose?",
     "options": json.dumps(["docker compose up -d", "docker run", "docker start", "docker build"]),
     "correct_answer": "docker compose up -d", "category": "devops"},
    {"content": "Pydantic dùng để làm gì trong FastAPI?",
     "options": json.dumps(["Validate dữ liệu request/response", "Kết nối database", "Xử lý authentication", "Build Docker image"]),
     "correct_answer": "Validate dữ liệu request/response", "category": "backend"},
    {"content": "GitHub Actions workflow được lưu ở đâu?",
     "options": json.dumps([".github/workflows/", "github/", ".actions/", "workflows/"]),
     "correct_answer": ".github/workflows/", "category": "devops"},
    {"content": "Biến môi trường trong Vite (React) phải bắt đầu bằng gì?",
     "options": json.dumps(["VITE_", "REACT_APP_", "ENV_", "PUBLIC_"]),
     "correct_answer": "VITE_", "category": "frontend"},
]

for q in questions_data:
    db.add(Question(**q))

quizzes_data = [
    {"title": "Bài thi DevOps cơ bản", "description": "Kiểm tra kiến thức DevOps, Docker, CI/CD"},
    {"title": "Bài thi Backend", "description": "FastAPI, SQLAlchemy, REST API"},
    {"title": "Bài thi tổng hợp", "description": "Tất cả chủ đề: DevOps, Backend, Frontend, Git"},
]

for quiz in quizzes_data:
    db.add(Quiz(**quiz))

db.commit()
db.close()

print("✅ Seed data thành công: 13 câu hỏi + 3 bài thi")