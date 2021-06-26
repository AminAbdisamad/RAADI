from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column ,String, Boolean, Integer, DateTime, Text
from database import Base, engine
from uuid import uuid4, UUID


def generate_uuid():
        return str(uuid4())

# creating Institution class

class Institution(Base):
    __tablename__ = 'institutions'
    id = Column(Integer, primary_key=True,  index=True)
    business_id = Column(String, index=True, default=generate_uuid)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)
    logo = Column(String, default='business_logo.png')
    phone = Column(Integer, index=True)
    email = Column(String, index=True)
    country = Column(String, index=True,nullable=False)
    city = Column(String, index = True,nullable=False)
    district = Column(String, index = True,nullable=False)
    address = Column(String, index=True)
    category = Column(String, index=True)
    website_url = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    # other attributes
    # owner,reviews, **rating
    
    

# Create Institutions Table
Base.metadata.create_all(bind=engine)

# ** Pydantic Models

class InstitutionsBase(BaseModel):
    class Config:
        orm_mode = True 
        
    name:str
    description:str
    phone:int
    logo:str
    email:str
    country:str
    city:str
    district:str
    address:str
    category:str
    website_url:Optional[str] = None
    

class InstitutionRegister(InstitutionsBase):
    pass

class InstitutionUpdate(InstitutionsBase):
    created_at:datetime

class InstitutionRead(InstitutionsBase):
    id : int
    business_id : str
    created_at : datetime
    updated_at : datetime