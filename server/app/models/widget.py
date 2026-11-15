"""Data models for mobile home screen widget payloads."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class WidgetStatusResponse(BaseModel):
    pet_name: str = Field(default="Mimi")
    current_status: str = Field(..., description="Short status text (e.g., 'Napping peacefully on a warm spot ☀️')")
    mood_emoji: str = Field(default="🐾", description="Emoji representation")
    energy_level: int = Field(default=85, ge=0, le=100, description="Percentage of energy/playfulness")
    affection_level: int = Field(default=100, ge=0, le=100, description="Affection indicator")
    quick_reminder: Optional[str] = Field(default=None, description="Optional gentle reminder or encouragement")
    last_updated: datetime = Field(default_factory=datetime.utcnow)
