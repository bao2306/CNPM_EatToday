from sqlalchemy import Column, Integer, String
from src.infrastructure.databases.db import Base

class MealModel(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=False)