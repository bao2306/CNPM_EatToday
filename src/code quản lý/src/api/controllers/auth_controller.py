from fastapi import HTTPException, Depends
from src.api.schemas.schemas import UserCreate, UserLogin
from sqlalchemy.orm import Session
from src.infrastructure.databases.db import get_db
from src.infrastructure.models.user_model import UserModel
from python_jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from src.config import Config

class AuthController:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = next(db)
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.SECRET_KEY = Config.SECRET_KEY
        self.ALGORITHM = "HS256"

    def register(self, user: UserCreate):
        existing_user = self.db.query(UserModel).filter(UserModel.username == user.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        hashed_password = self.pwd_context.hash(user.password)
        db_user = UserModel(username=user.username, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return {"message": "User registered successfully"}

    def login(self, user: UserLogin):
        db_user = self.db.query(UserModel).filter(UserModel.username == user.username).first()
        if not db_user or not self.pwd_context.verify(user.password, db_user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        payload = {
            "user_id": db_user.id,
            "exp": datetime.utcnow() + timedelta(hours=2)
        }
        token = jwt.encode(payload, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return {"token": token}