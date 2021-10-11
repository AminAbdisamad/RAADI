from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base, engine
from database.core import DateTimeMixin, RaadiBase
from users.model import User
# from Institutions.model import Institution

# fixing review add issue
class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    review_comment = Column(Text)
    review_stars = Column(Integer) 
    user_id = Column(Integer, ForeignKey("users.id"))
    institution_id = Column(Integer, ForeignKey("institutions.id")) 
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
  
   


Base.metadata.create_all(bind=engine)

# ** Pydantic Models

class ReviewBase(RaadiBase):
    review_comment:str
    review_stars:int

class ReviewRegister(ReviewBase):
    userId:int
    institutionId:int
    pass


class ReviewUpdate(ReviewBase):
    updated_at: datetime


class ReviewRead(ReviewBase):
    institutionId:int
    userId:int
    review_owner:User
    # review_institution:Institution
    id: int
    created_at: datetime
    updated_at: datetime
