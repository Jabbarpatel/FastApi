from fastapi import APIRouter
from typing import Union
from db.db import DB
from documentation.documents import AddNewUser

user_route = APIRouter()

@user_route.get('/get_users')
@user_route.get('/get_users/{page}/{page_size}')
@user_route.get('/get_users/{page}/{page_size}/{filter}')
def get_users(page:int=None,page_size:int = None,filter:Union[str,int]=None):
    try:
       res_list = DB.get_user_data(page,page_size,filter)
       if res_list:
           return res_list
       else:
           return str('User list is not found'),200
    except Exception as e:
        print(e)
        return 'error',500
    
@user_route.delete('/delete_user/{idx}')
def delete_user(idx:int = None):
    try:
        if idx:
            DB.delete_user(idx)
            return 'success',200
        
    except Exception as e:
        print(e)
        return str(e),500
    
@user_route.post('/add_user')
def add_user(request:AddNewUser):
    try:
        idx = request.idx
        first_name = request.first_name
        last_name = request.last_name
       
        if idx and first_name and last_name:
            pass
        
    except Exception as e:
        print(e)
        return 'error',500