from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# ------------------------------
# Database setup
# ------------------------------
DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ------------------------------
# Models
# ------------------------------
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    fullname = Column(String, default="")
    history = relationship("History", back_populates="owner")

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    detail = Column(String)

class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    owner = relationship("User", back_populates="history")

Base.metadata.create_all(bind=engine)

# ------------------------------
# Schemas
# ------------------------------
class UserCreate(BaseModel):
    username: str
    password: str
    fullname: str = ""

class UserLogin(BaseModel):
    username: str
    password: str

class RecipeCreate(BaseModel):
    title: str
    detail: str

class RecipeOut(BaseModel):
    id: int
    title: str
    detail: str
    class Config:
        orm_mode = True

# ------------------------------
# FastAPI app
# ------------------------------
app = FastAPI(title="EatToday Backend API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------
# Routes
# ------------------------------

@app.get("/")
def root():
    return {"message": "EatToday Backend API is running!"}

# Đăng ký
@app.post("/signup")
def signup(user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = User(username=user.username, password=user.password, fullname=user.fullname)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}

# Đăng nhập
@app.post("/login")
def login(user: UserLogin):
    db = SessionLocal()
    db_user = db.query(User).filter(User.username == user.username, User.password == user.password).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful", "user_id": db_user.id, "fullname": db_user.fullname}

# Hồ sơ cá nhân
@app.get("/profile/{user_id}")
def profile(user_id: int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": db_user.id, "username": db_user.username, "fullname": db_user.fullname}

# Thêm công thức nấu ăn
@app.post("/recipes", response_model=RecipeOut)
def add_recipe(recipe: RecipeCreate):
    db = SessionLocal()
    new_recipe = Recipe(title=recipe.title, detail=recipe.detail)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

# Lấy danh sách công thức
@app.get("/recipes", response_model=List[RecipeOut])
def get_recipes():
    db = SessionLocal()
    recipes = db.query(Recipe).all()
    return recipes

# Gợi ý thực đơn (giả sử lấy ngẫu nhiên)
@app.get("/suggest/{user_id}", response_model=List[RecipeOut])
def suggest_menu(user_id: int):
    db = SessionLocal()
    recipes = db.query(Recipe).all()
    return recipes[:3]  # tạm gợi ý 3 món đầu tiên

# Lịch sử món ăn
@app.post("/history/{user_id}/{recipe_id}")
def add_history(user_id: int, recipe_id: int):
    db = SessionLocal()
    history = History(user_id=user_id, recipe_id=recipe_id)
    db.add(history)
    db.commit()
    return {"message": "Added to history"}

@app.get("/history/{user_id}")
def get_history(user_id: int):
    db = SessionLocal()
    history = db.query(History).filter(History.user_id == user_id).all()
    return [{"recipe_id": h.recipe_id} for h in history]
