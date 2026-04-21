from pydantic import BaseModel
from typing import List

class UserLists(BaseModel):
    users: List[str]
