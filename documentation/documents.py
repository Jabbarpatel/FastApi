from pydantic import BaseModel
from typing import Union,Optional

class AddNewUser(BaseModel):
    idx:int = None
    first_name:str = None
    last_name:str = None
    
    