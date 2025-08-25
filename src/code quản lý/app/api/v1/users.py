
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...schemas.user import UserRead, UserUpdate
from ...models.user import User
from ..deps import get_db, get_current_user
from ...core.security import get_password_hash

router = APIRouter()

@router.get("/me", response_model=UserRead)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserRead)
def update_me(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if data.email is not None:
        current_user.email = data.email
    if data.full_name is not None:
        current_user.full_name = data.full_name
    if data.password:
        current_user.hashed_password = get_password_hash(data.password)

    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
