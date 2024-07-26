
class DeleteUserExeception(Exception):
    def __init__(self,idx):
        super().__init__(f'Record doesnot exists with idx {idx}')
        
class UserAlreadyExistsExeception(Exception):
    def __init__(self,idx):
        super().__init__(f'This user exists with {idx}')