from fastapi import APIRouter, Depends
from app.api.deps import get_memory_service
from app.services.memory_service import MemoryService
from app.schemas.users import UserLists


router = APIRouter(prefix='/users', tags=['users'])

@router.get("", response_model=UserLists)
def list_users(memory:MemoryService=Depends(get_memory_service)):
    return {"users": memory.get_all_users()}


@router.post("/")
def create_user(memory:MemoryService=Depends(get_memory_service)):
    return memory.create_new_user()

@router.delete("/{user_id}")
def delete_user(user_id: str, memory: MemoryService=Depends(get_memory_service)):
    return memory.delete(user_id)
