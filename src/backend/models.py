from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(255))
    preferences = Column(Text, nullable=True)  
    budget = Column(Float, nullable=True)

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    description = Column(Text)
    nutrition = Column(Text)
