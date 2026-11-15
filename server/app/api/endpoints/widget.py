"""Endpoints for home screen widget synchronization."""

import random
from fastapi import APIRouter
from app.models.widget import WidgetStatusResponse

router = APIRouter(prefix="/widget", tags=["Widget"])

STATUSES = [
    ("Napping peacefully in a patch of sunshine ☀️", "😴", 70, "Take a restful breath."),
    ("Watching birds outside the window! 🐦", "👀", 95, "Stay curious today!"),
    ("Curled up contentedly, purring softly 🐾", "🤍", 80, "Drink a glass of water."),
    ("Stretching tiny paws and thinking of you ✨", "🐾", 85, "You've got this!"),
    ("Ready for playtime and gentle pats! 🧶", "😺", 90, "Remember to smile today."),
]


@router.get("/status", response_model=WidgetStatusResponse)
async def get_widget_status():
    """Returns the current state for iOS WidgetKit / Android AppWidget."""
    status, emoji, energy, reminder = random.choice(STATUSES)
    return WidgetStatusResponse(
        pet_name="Mimi",
        current_status=status,
        mood_emoji=emoji,
        energy_level=energy,
        affection_level=100,
        quick_reminder=reminder
    )
