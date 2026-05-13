from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from typing import List
import json

router = APIRouter(prefix="/api/results", tags=["results"])

@router.post("/submit", response_model=schemas.ResultOut)
def submit_quiz(payload: schemas.SubmitQuizIn, db: Session = Depends(get_db)):
    quiz = db.query(models.Quiz).filter(models.Quiz.id == payload.quiz_id).first()
    result = models.Result(quiz_id=payload.quiz_id, total_questions=len(payload.answers))
    db.add(result)
    db.flush()

    correct = 0
    for ans in payload.answers:
        q = db.query(models.Question).filter(models.Question.id == ans.question_id).first()
        is_correct = q.correct_answer == ans.selected_option if q else False
        if is_correct:
            correct += 1
        db.add(models.Answer(
            question_id=ans.question_id,
            selected_option=ans.selected_option,
            is_correct=is_correct,
            result_id=result.id
        ))

    result.score = (correct / len(payload.answers)) * 100 if payload.answers else 0
    db.commit()
    db.refresh(result)
    return result

@router.get("/", response_model=List[schemas.ResultOut])
def get_results(db: Session = Depends(get_db)):
    return db.query(models.Result).all()