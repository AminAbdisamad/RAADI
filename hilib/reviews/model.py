from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, Text
from database import Base, engine
from database.core import DateTimeMixin, RaadiBase


class Review(Base, DateTimeMixin):
    __tablename__: "reviews"
    id = Column(Integer, primary_key=True, index=True)
    review_comment = Column(Text)
    review_stars = Column(Integer) 


Base.metadata.create_all(bind=engine)

# ** Pydantic Models

class ReviewBase(BaseModel,RaadiBase):
    review_comment:str
    review_stars:int

class ReviewRegister(UserBase):
    pass


class ReviewUpdate(UserBase):
    updated_at: datetime


class ReviewRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
