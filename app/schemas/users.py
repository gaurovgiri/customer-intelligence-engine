from pydantic import BaseModel
from typing import List

class UserLists(BaseModel):
    users: List[str]


class CreateUserResponse(BaseModel):
    user_id: str


class DeleteUserResponse(BaseModel):
    deleted: bool
