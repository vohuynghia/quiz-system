from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    options = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    category = Column(String, default="general")
    answers = relationship("Answer", back_populates="question")

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    results = relationship("Result", back_populates="quiz")

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Float, default=0.0)
    total_questions = Column(Integer)
    completed_at = Column(DateTime, default=datetime.utcnow)
    quiz = relationship("Quiz", back_populates="results")
    answers = relationship("Answer", back_populates="result")

class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    result_id = Column(Integer, ForeignKey("results.id"))
    selected_option = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)
    question = relationship("Question", back_populates="answers")
    result = relationship("Result", back_populates="answers")