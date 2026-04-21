from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.chat_models import BaseChatModel
from app.services.memory_service import MemoryService
from app.services.intent_service import IntentService
from app.prompts.chat_prompt import SYSTEM_PROMPT_TEMPLATE
from app.data.price import PRICE_TABLE
import json

class ChatService:
    def __init__(self, llm: BaseChatModel, memory:MemoryService, intent_service:IntentService):
        self.llm = llm
        self.memory = memory
        self.intent_model = intent_service

    def _build_user_message(self, message:str) -> HumanMessage:
        intent, confidence = self.intent_model.predict(message)
        if not intent:
            intent = ''
        if not confidence:
            confidence = 0.0
            
        message = f"""
        User Message: {message}
        ---
        Intent: {intent}
        Confidence: {confidence}
        """
        return HumanMessage(message), intent, confidence

    def generate_response(self, user, message):
        if not self.memory.get(user):
            system_prompt = SYSTEM_PROMPT_TEMPLATE.format(price_table=json.dumps(PRICE_TABLE))
            self.memory.save(user, SystemMessage(system_prompt))

        message, intent, confidence = self._build_user_message(message)

        self.memory.save(user, message)

        history = self.memory.get(user)
        
        response = self.llm.invoke(history)

        if isinstance(response.content, list):
            for resp in response.content:
                if resp.get('type') == 'text':
                    response = AIMessage(resp['text'])
                    break
            
        self.memory.save(user, response)

        return {
            "message": response.content,
            "intent": intent,
            "confidence": confidence
            }