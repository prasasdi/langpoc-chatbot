from fastapi import APIRouter
from app.services.langgraph_service import run_graph
from app.schemas.chat_schema import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    response = run_graph(req.message)
    return ChatResponse(reply=response)
