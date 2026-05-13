from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from typing import List

router = APIRouter(prefix="/api/quizzes", tags=["quizzes"])

@router.get("/", response_model=List[schemas.QuizOut])
def get_quizzes(db: Session = Depends(get_db)):
    return db.query(models.Quiz).all()

@router.post("/", response_model=schemas.QuizOut)
def create_quiz(quiz: schemas.QuizCreate, db: Session = Depends(get_db)):
    new_quiz = models.Quiz(**quiz.dict())
    db.add(new_quiz)
    db.commit()
    db.refresh(new_quiz)
    return new_quiz