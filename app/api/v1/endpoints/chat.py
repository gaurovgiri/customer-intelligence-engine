from fastapi import APIRouter, Depends
from app.services.chat_service import ChatService
from app.schemas.chat import ChatRequest, ChatResponse
from app.api.deps import get_chat_service

router = APIRouter(prefix="/chat", tags=['chat'])

@router.post("/", response_model=ChatResponse)
def chat(req: ChatRequest, chat_service:ChatService=Depends(get_chat_service)):
    return {"message": chat_service.generate_response(user=req.user_id, message=req.message)}
