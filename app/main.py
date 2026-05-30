from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse
from app.bot_service import BotService
from app.settings import settings

app = FastAPI(title=settings.app_name)
bot_service = BotService()


@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return bot_service.handle_question(request.question)