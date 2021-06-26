from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import Base, SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Save to database
def save(db: Session, data: object):
    db.add(data)
    db.commit()
    db.refresh(data)


class DateTimeMixin:
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)


# Pydantic basemodel
class RaadiBase(BaseModel):
    class Config:
        orm_mode = True
