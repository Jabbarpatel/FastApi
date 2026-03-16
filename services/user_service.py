from repository.user_repo import UserRepository
from execeptions.execeptions import UserAlreadyExists, UserNotFound

repo = UserRepository()


class UserService:
    @staticmethod
    def get_users():
        users = repo.get_users()
        return [
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
            for user in users
        ]

    @staticmethod
    def create_user(first_name: str, last_name: str):
        user = repo.get_user_by_name(first_name)
        if user is not None:
            raise UserAlreadyExists(first_name)

        repo.add_user(first_name, last_name)

    @staticmethod
    def delete_user(id: int):
        user = repo.get_user_by_id(id)
        if user is None:
            raise UserNotFound()

        repo.delete_user(user)

    @staticmethod
    def update_user(id: int, first_name: str, last_name: str):
        user = repo.get_user_by_id(id)
        if user is None:
            raise UserNotFound()

        repo.update_user(user, first_name, last_name)
