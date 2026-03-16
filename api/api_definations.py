from pydantic import BaseModel, Field


class GetAllUserResponse(BaseModel):
    id: int = Field(example=1)
    first_name: str = Field(example="Jabbar")
    last_name: str = Field(exampl="Patel")


class CreateUserRequest(BaseModel):
    first_name: str = Field(example="Jabbar")
    last_name: str = Field(exampl="Patel")


class UpdateUserRequest(BaseModel):
    id: int = Field(example=1)
    first_name: str = Field(example="Jabbar")
    last_name: str = Field(exampl="Patel")
