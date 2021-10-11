from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from typing import Optional
from users.model import User, UserRegister, UserRead, UserUpdate


# Get All Users
def get_all_users(db: Session) -> list[Optional[User]]:
    """Returns all users"""
    return db.query(User).all()


# Get User by username
def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """Gets user by username"""
    return db.query(User).filter(User.username == username).one_or_none()


# Add a user to the database
def create_user(*, db: Session, user: UserRegister) -> Optional[User]:
    """Creates new user"""
    # check if the username is already exist
    user_in_db = get_user_by_username(db, user.username)
    if user_in_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with that username already exist, please try different username",
        )
    user = User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user




# pk, starts-1-5, review, review_count ,institution_id, user_id,create_at, updated_at,