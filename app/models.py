from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class ChatRequest(BaseModel):
    user_id: str
    question: str


class ConnectorResult(BaseModel):
    source: str
    success: bool
    data: Dict[str, Any] = {}
    error: Optional[str] = None


class ChatResponse(BaseModel):
    bot_name: str
    style: str
    answer: str
    sources: List[str]
    details: Dict[str, Any]