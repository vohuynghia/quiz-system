from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from typing import List

router = APIRouter(prefix="/api/questions", tags=["questions"])

@router.get("/", response_model=List[schemas.QuestionOut])
def get_questions(db: Session = Depends(get_db)):
    return db.query(models.Question).all()

@router.post("/", response_model=schemas.QuestionOut)
def create_question(q: schemas.QuestionCreate, db: Session = Depends(get_db)):
    question = models.Question(**q.model_dump())
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

@router.get("/{question_id}", response_model=schemas.QuestionOut)
def get_question(question_id: int, db: Session = Depends(get_db)):
    q = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return q