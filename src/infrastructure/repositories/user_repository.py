from ..model.user_model import User
from ..database.base import db

class UserRepository:
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def add_user(self, user):
        db.session.add(user)
        db.session.commit()