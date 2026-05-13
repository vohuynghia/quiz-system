from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class QuestionBase(BaseModel):
    content: str
    options: str
    correct_answer: str
    category: str = "general"

class QuestionCreate(QuestionBase): pass

class QuestionOut(QuestionBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class QuizCreate(BaseModel):
    title: str
    description: Optional[str] = None

class QuizOut(QuizCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime

class AnswerIn(BaseModel):
    question_id: int
    selected_option: str

class SubmitQuizIn(BaseModel):
    quiz_id: int
    answers: List[AnswerIn]

class ResultOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    quiz_id: int
    score: float
    total_questions: int
    completed_at: datetime