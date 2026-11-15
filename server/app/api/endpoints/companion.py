"""Endpoints for interacting with Mimi as an AI companion."""

from fastapi import APIRouter
from app.models.chat import ChatRequest, ChatResponse, DailyGreetingResponse
from app.services.mimi_ai import mimi_ai_service

router = APIRouter(prefix="/companion", tags=["Companion"])


@router.post("/chat", response_model=ChatResponse)
async def chat_with_mimi(request: ChatRequest):
    """Send a message to Mimi and receive her gentle, playful response."""
    return await mimi_ai_service.generate_reply(
        message=request.message,
        conversation_history=request.conversation_history,
        user_name=request.user_name
    )


@router.get("/greeting", response_model=DailyGreetingResponse)
async def get_daily_greeting():
    """Retrieve Mimi's warm daily greeting and thought for the day."""
    return await mimi_ai_service.get_daily_greeting()
