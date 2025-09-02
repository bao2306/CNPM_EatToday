from sqlalchemy import Column, Integer, String, ForeignKey
from src.infrastructure.databases.db import Base

class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    task = Column(String, nullable=False)