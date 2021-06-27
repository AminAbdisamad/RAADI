from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from institutions.model import Institution, InstitutionRegister, InstitutionRead
from institutions.service import create_institution, get_all_institutions
from database.core import get_db

institutions = APIRouter(prefix="/api/V1/institutions")


@institutions.post("/")
def add_institution(
    institution: InstitutionRegister, db: Session = Depends(get_db)
) -> Institution:
    new_institution = create_institution(db=db, institution=institution)
    return new_institution


# ** get all Institutions
@institutions.get("/")
def get_institutions(db: Session = Depends(get_db)) -> list[Optional[Institution]]:
    return get_all_institutions(db=db)
