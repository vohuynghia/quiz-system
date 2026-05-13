import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import questions, quizzes, results, auth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quiz System API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # sẽ chỉnh lại khi deploy
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questions.router)
app.include_router(quizzes.router)
app.include_router(results.router)
app.include_router(auth.router)

@app.get("/api/health")
def health_check():
    logger.info("Health check called")
    return {"ok": True}