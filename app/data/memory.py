from uuid import uuid4
from typing import Dict, Any, List
from pydantic import BaseModel, Field

class UserData(BaseModel):
    messages: List[Any]


class Memory(BaseModel):
    user: Dict[str, UserData] = Field(default_factory=dict)
    


class MemoryRepository:

    def __init__(self):
        self._id = uuid4()
        self._memory = Memory()

    def get(self, user):
        """Return stored messages for a user."""
        user_data = self._memory.user.get(user)
        if user_data is not None:
            return user_data.messages
        return []

    def save(self, user, message):
        """Save a message for a user."""
        try:
            if user not in self._memory.user:
                self._memory.user[user] = UserData(messages=[], timeout=0)

            self._memory.user[user].messages.append(message)
            return True
        except Exception as e:
            raise e

    def delete(self, user):
        """Delete a user from memory."""
        if user in self._memory.user:
            del self._memory.user[user]
            return True
        return False