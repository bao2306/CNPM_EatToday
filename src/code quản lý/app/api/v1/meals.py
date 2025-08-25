
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...schemas.meal import MealCreate, MealRead
from ...models.meal import Meal
from ...models.user import User
from ..deps import get_db, get_current_user
from ...services.suggestions import suggest_by_history

router = APIRouter()

@router.post("/meals", response_model=MealRead, status_code=201)
def add_meal(
    meal_in: MealCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    meal = Meal(user_id=current_user.id, meal_name=meal_in.meal_name)
    db.add(meal)
    db.commit()
    db.refresh(meal)
    return meal

@router.get("/meals", response_model=List[MealRead])
def list_meals(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    items = db.query(Meal).filter(Meal.user_id == current_user.id).order_by(Meal.eaten_at.desc()).all()
    return items

@router.get("/suggest")
def suggest(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    suggestion = suggest_by_history(db, current_user.id)
    return {"suggestion": suggestion}
