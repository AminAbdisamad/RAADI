from sqlalchemy.orm import Session
from typing import Optional
from reviews.model import (
    ReviewRegister,
    ReviewRead,
    Review,
    ReviewUpdate
    
)

# ** get all reviews

def get_all_reviews(db:Session)-> list[Optional[Review]]:
    return db.query(Review).all()


# ** create review

def create_review(db: Session, review:Review) -> Review:
    review = Review(**review.dict())
    db.add(review)
    db.commit()
    db.refresh(review)
    return review
