"""Pydantic models for user management endpoints."""

from pydantic import BaseModel
from typing import List

class UserLists(BaseModel):
    """Response payload containing all user IDs."""

    users: List[str]


class CreateUserResponse(BaseModel):
    """Response payload returned after user creation."""

    user_id: str


class DeleteUserResponse(BaseModel):
    """Response payload indicating delete outcome."""

    deleted: bool
