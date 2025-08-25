
from sqlalchemy.orm import Session
from ..models.meal import Meal

DEFAULTS = ["Phở bò", "Cơm tấm", "Bánh mì trứng", "Gỏi cuốn", "Bún chả", "Bún bò Huế", "Hủ tiếu"]

def suggest_by_history(db: Session, user_id: int) -> str:
    # Rất đơn giản: ưu tiên món chưa ăn trong 3 ngày gần nhất
    recent = db.query(Meal).filter(Meal.user_id == user_id).order_by(Meal.eaten_at.desc()).limit(10).all()
    recent_names = {m.meal_name for m in recent}
    for name in DEFAULTS:
        if name not in recent_names:
            return name
    # nếu tất cả đã ăn gần đây, trả món mặc định
    return DEFAULTS[0]
