
from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db.session import Base

class Meal(Base):
    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    meal_name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    eaten_at: Mapped = mapped_column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="meals")
