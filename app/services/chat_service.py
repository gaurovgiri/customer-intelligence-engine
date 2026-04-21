from app.llm.factory import LLMFactory

class ChatService:
    def __init__(self, llm, memory):
        self.llm = llm
        self.memory = memory

    def generate_response(self, user, message):
        # store user message
        self.memory.save(user, message)

        # get history
        history = self.memory.get(user)

        # call LLM
        response = self.llm.invoke(history)

        # store assistant response
        self.memory.save(user, response)

        return response.content