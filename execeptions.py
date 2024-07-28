
class UserNotFoundExeception(Exception):
    def __init__(self,idx):
        super().__init__(f'Record doesnot exists with idx {idx}')
        
class UserAlreadyExistsExeception(Exception):
    def __init__(self,idx):
        super().__init__(f'This user already exists with id {idx}')

class UserIdxListNotFound(Exception):
    def __init__(self):
        super().__init__(f'User idx list not found')
