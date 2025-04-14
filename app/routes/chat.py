from fastapi import APIRouter
from app.services.lang_service import run_graph
from app.schemas.chat_schema import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    print("masuk sini")
    response = run_graph(req.message)
    print("run graph")
    return ChatResponse(reply=response)
