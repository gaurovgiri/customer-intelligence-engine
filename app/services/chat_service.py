from app.llm.factory import LLMFactory
from app.data.memory import MemoryRepository
class ChatService:

    def __init__(self, provider:str="GEMINI", memory_repo:MemoryRepository=None):
        self.llm = LLMFactory.create(provider)
        if memory_repo:
            self.memory = memory_repo
        else:
            self.memory = MemoryRepository()

    def respond(self, user, message):
        if self.memory.save(user, message):
            history = self.memory.get(user)
            response = self.llm.invoke(history)
            self.memory.save(user, response)
            return response.content

        raise RuntimeError("Error saving the message for the user")


if __name__ == "__main__":
    import uuid

    chat = ChatService()
    user = uuid.uuid4()
    response = chat.respond(
        user, "My name is Gaurav Giri."
    )
    print(response)
    response = chat.respond(
        user, "Who am I?"
    )
    print(response)