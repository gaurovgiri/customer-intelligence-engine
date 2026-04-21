"""In-memory conversation state storage by user identifier."""

from uuid import uuid4
from typing import Dict, List
from langchain_core.messages import BaseMessage

class MemoryService:
    """Manage chat history for each user in process memory."""

    def __init__(self):
        """Initialize an empty user-to-message map."""
        self._id = uuid4()
        self._memory: Dict[str, List[BaseMessage]] = {}

    def get(self, user: str) -> List[BaseMessage]:
        """Return message history for a user, or an empty list if absent."""
        return self._memory.get(user, [])
    
    def create_new_user(self) -> str:
        """Create a new user id and initialize empty history for it."""
        new_user = uuid4()
        new_user = str(new_user)
        self._memory[new_user] = []
        return new_user

    def save(self, user: str, message: BaseMessage):
        """Append a message to a user's history."""
        if user not in self._memory:
            raise RuntimeError("This user doesn't exists! Create a new user!")
        self._memory[user].append(message)

    def delete(self, user: str):
        """Delete a user's history and return whether deletion happened."""
        return self._memory.pop(user, None) is not None

    def get_all_users(self):
        """List all known user identifiers."""
        return [str(ids) for ids in self._memory.keys()]

