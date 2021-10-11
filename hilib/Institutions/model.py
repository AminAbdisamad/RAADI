from typing import Optional
from datetime import datetime
from uuid import uuid4, UUID
from pydantic import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine
from database.core import RaadiBase, DateTimeMixin
from users.model import User
# from reviews.model import Review


# generate UUID
def generate_uuid():
    return str(uuid4())


# creating Institution class


class Institution(Base):
    __tablename__ = "institutions"
    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(String, index=True, default=generate_uuid)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)
    logo = Column(String, default="business_logo.png", nullable=False)
    phone = Column(Integer, index=True)
    email = Column(String, index=True)
    category = Column(String, index=True)
    website_url = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))
    reviews = relationship('Review', backref="reviews")
  
# Create Institutions Table
Base.metadata.create_all(bind=engine)

# ** Pydantic Models


class InstitutionsBase(RaadiBase):
    name: str
    description: str
    phone: int
    logo: str
    email: str
    country: str
    # city: str
    # district: str
    # address: str
    category: str
    user_id:int
    website_url: Optional[str] = None


class InstitutionRegister(InstitutionsBase):
    user_id:int
    pass


class InstitutionUpdate(InstitutionsBase):
    created_at: datetime


class InstitutionRead(InstitutionsBase):
    id: int
    user_id:int
    institution_owner:User
    business_id: str
    created_at: datetime
    updated_at: datetime
