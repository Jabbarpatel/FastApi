from execeptions.app_exeception import AppExeception


class UserAlreadyExists(AppExeception):
    def __init__(self, name: str):
        super().__init__(f"User with name {name} is already exists!", 409)


class UserNotFound(AppExeception):
    def __init__(self):
        super().__init__("User not found!", 409)
