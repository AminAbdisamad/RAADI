from sqlalchemy.orm import Session
from typing import Optional
from Institutions.model import (
    Institution,
    InstitutionRead,
    InstitutionRegister,
    InstitutionUpdate,
)

# ** create a Institution
def create_institution(db: Session, institution: InstitutionRegister) -> Institution:
    institution = Institution(**institution.dict())
    db.add(institution)
    db.commit()
    db.refresh(institution)
    return institution


# ** get all Instituitons
def get_all_institutions(db: Session) -> list[Optional[Institution]]:
    return db.query(Institution).all()
