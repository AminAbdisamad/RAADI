from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from sqlalchemy import Column, String, Integer, Boolean, Text, DateTime
from sqlalchemy.orm import relationship

from database import Base, engine
from database.core import DateTimeMixin, RaadiBase



# ** User Model


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True, nullable=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, index=True)
    password = Column(String, nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    avatar = Column(String, default="avatar.png")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    
    # user_reviews = relationship('Review', back_populates="review_owner")
    institutions = relationship('Institution', back_populates="institution_owner")


# Create Users Table
Base.metadata.create_all(bind=engine)

# ** Pydantic Models
class UserBase(RaadiBase):
    class Config:
        orm_mode = True

    full_name: Optional[str] = None
    username: str
    email: str
    password: str
    phone: Optional[str] = None
    description: Optional[str] = None
    avatar: Optional[str] = None
    is_admin: Optional[bool] = False
    is_active: Optional[bool] = True


class UserRegister(UserBase):
    pass


class UserUpdate(UserBase):
    updated_at: datetime


class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
