from uuid import uuid4
from typing import Dict, Any, List
from langchain_core.messages import BaseMessage

class MemoryService:
    def __init__(self):
        self._id = uuid4()
        self._memory: Dict[str, List[BaseMessage]] = {}

    def get(self, user: str) -> List[BaseMessage]:
        return self._memory.get(user, [])
    
    def create_new_user(self) -> str:
        new_user = uuid4()
        new_user = str(new_user)
        self._memory[new_user] = []
        return new_user

    def save(self, user: str, message: BaseMessage):
        if user not in self._memory:
            raise RuntimeError("This user doesn't exists! Create a new user!")
        self._memory[user].append(message)

    def delete(self, user: str):
        return self._memory.pop(user, None) is not None

    def get_all_users(self):
        return [str(ids) for ids in self._memory.keys()]

