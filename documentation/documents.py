from pydantic import BaseModel,Field
from typing import Union,Optional

class AddNewUser(BaseModel):
    idx:int = None
    first_name:str = Field(...,description='First name must be string')
    last_name:str = Field(...,description='Last name must be string')
    
class UpdateUser(BaseModel):
    first_name:str
    last_name:str
    
    
