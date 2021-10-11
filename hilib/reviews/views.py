from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from reviews.model import Review, ReviewRegister, ReviewUpdate
from reviews.service import create_review, get_all_reviews
from database.core import get_db

reviews = APIRouter(prefix="/api/v1/reviews")


@reviews.post("/")
def add_institution(
    review: ReviewRegister, db: Session = Depends(get_db)
) -> Review:
    new_review = create_review(db=db, review=review)
    return new_review


# ** get all Reviews
@reviews.get("/")
def get_reviews(db: Session = Depends(get_db)) -> list[Optional[Review]]:
    return get_all_reviews(db=db)
