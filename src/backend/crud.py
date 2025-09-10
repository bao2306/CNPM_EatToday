from sqlalchemy.orm import Session
from . import models, schemas

# -------------------- User --------------------
def create_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        return None
    new_user = models.User(
        username=user.username,
        password=user.password,
        fullname=user.fullname
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(db: Session, user: schemas.UserLogin):
    return db.query(models.User).filter(
        models.User.username == user.username,
        models.User.password == user.password
    ).first()

# -------------------- Recipe --------------------
def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    new_recipe = models.Recipe(
        name=recipe.name,
        description=recipe.description,
        nutrition=recipe.nutrition
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

def get_recipes(db: Session):
    return db.query(models.Recipe).all()

# -------------------- History --------------------
def add_history(db: Session, user_id: int, recipe_id: int):
    history = models.History(user_id=user_id, recipe_id=recipe_id)
    db.add(history)
    db.commit()
    return history

def get_history(db: Session, user_id: int):
    return db.query(models.History).filter(models.History.user_id == user_id).all()

