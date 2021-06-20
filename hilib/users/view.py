from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from users.model import UserRegister, UserRead, User
from users.service import create_user, get_all_users, get_user_by_username
from database.core import get_db

users = APIRouter(prefix="/api/v1/users")

# Create User Route
@users.post("/")
def add_user(user: UserRegister, db: Session = Depends(get_db)) -> Optional[User]:
    user_in_db = create_user(db=db, user=user)
    return user_in_db


# Get All Users Route
@users.get("/")
def get_users(db: Session = Depends(get_db)) -> list[Optional[User]]:
    return get_all_users(db=db)


# Get User By username Route
@users.get("/{username}")
def get_by_username(db: Session = Depends(get_db), username=str):
    return get_user_by_username(db=db, username=username)
