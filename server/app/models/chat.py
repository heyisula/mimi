"""Data models for chat and companion interactions."""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class MessageItem(BaseModel):
    role: str = Field(..., description="'user' or 'mimi'")
    content: str = Field(..., description="Message text content")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000, description="User's input message")
    conversation_history: Optional[List[MessageItem]] = Field(default=None, description="Previous messages")
    user_name: Optional[str] = Field(default=None, description="User's preferred display name")


class ChatResponse(BaseModel):
    reply: str = Field(..., description="Mimi's response")
    mood: str = Field(default="happy", description="Mimi's current mood (happy, sleepy, curious, playful, purring)")
    animation_trigger: Optional[str] = Field(default="paw_tap", description="Animation hint for client widget or avatar")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class DailyGreetingResponse(BaseModel):
    greeting: str
    mood: str
    thought_of_the_day: str
    suggested_actions: List[str]
