import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = int(os.getenv("PORT", 8000))
    HOST = os.getenv("HOST", "0.0.0.0")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///eat_today.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")