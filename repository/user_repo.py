from models.users import Users
from config.connection import session


class UserRepository:
    def __init__(self):
        self.session = session

    def get_users(self) -> list[Users]:
        return self.session.query(Users).all()

    def get_user_by_name(self, name: str) -> Users:
        return self.session.query(Users).filter(Users.first_name == name).first()

    def get_user_by_id(self, id: int) -> Users:
        return self.session.query(Users).filter(Users.id == id).first()

    def delete_user(
        self,
        user: Users,
    ) -> None:
        self.session.delete(user)
        self.session.commit()

    def add_user(self, first_name: str, last_name: str) -> None:
        new_user = Users(first_name=first_name, last_name=last_name)
        self.session.add(new_user)
        self.session.commit()

    def update_user(self, user: Users, first_name: str, last_name: str):
        user.first_name = first_name
        user.last_name = last_name
        self.session.commit()
