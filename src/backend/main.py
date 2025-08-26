from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, database

app = FastAPI(title="EatToday Backend API")

# Tạo DB
models.Base.metadata.create_all(bind=database.engine)
#đăng kí router
app.include_router(api_router)
# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "EatToday Backend API is running!"}

# ---------------- Routes ----------------

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.create_user(db, user)
    if not new_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return {"message": "User created successfully", "user_id": new_user.id}

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.login_user(db, user)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful", "user_id": db_user.id, "fullname": db_user.fullname}

@app.get("/recipes", response_model=List[schemas.RecipeOut])
def get_recipes(db: Session = Depends(get_db)):
    return crud.get_recipes(db)

@app.post("/recipes", response_model=schemas.RecipeOut)
def add_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe)

@app.post("/history/{user_id}/{recipe_id}")
def add_history(user_id: int, recipe_id: int, db: Session = Depends(get_db)):
    crud.add_history(db, user_id, recipe_id)
    return {"message": "Added to history"}

@app.get("/history/{user_id}")
def get_history(user_id: int, db: Session = Depends(get_db)):
    history = crud.get_history(db, user_id)
    return [{"recipe_id": h.recipe_id} for h in history]
