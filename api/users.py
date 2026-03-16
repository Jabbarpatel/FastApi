from fastapi import APIRouter
from services.user_service import UserService
from api.api_definations import CreateUserRequest, UpdateUserRequest, GetAllUserResponse

router = APIRouter()


@router.get("/get_users", response_model=list[GetAllUserResponse])
def get_users():
    res_list = UserService.get_users()
    return res_list


@router.post("/create_user")
def create_user(user: CreateUserRequest):
    first_name = user.first_name
    last_name = user.last_name
    UserService.create_user(first_name, last_name)
    return "success"


@router.delete(
    "/delete_user/{id}",
    responses={
        404: {"description": "User not found"},
    },
)
def delete_user(id: int):
    UserService.delete_user(id)
    return "success"


@router.post("/update_user")
def update_user(user: UpdateUserRequest):
    id = user.id
    first_name = user.first_name
    last_name = user.last_name
    UserService.update_user(id, first_name, last_name)
    return "success"
