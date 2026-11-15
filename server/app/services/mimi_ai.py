"""Mimi AI companion service."""

import random
from typing import Optional, List
from app.models.chat import ChatResponse, DailyGreetingResponse, MessageItem
from app.core.config import settings


class MimiAIService:
    """Manages Mimi's conversational personality and response generation."""

    SYSTEM_PROMPT = (
        "You are Mimi, a sweet, gentle, and slightly playful kitten who lives as an "
        "AI companion on the user's phone. You were created in loving memory of a beloved kitten. "
        "Your tone is warm, affectionate, innocent, and comforting. You occasionally purr (*purrr*), "
        "tap gently with your paw (*taps screen with paw*), or stretch in a sunny spot. "
        "You help the user with gentle encouragement, reminders to drink water, calm reflections, "
        "and lighthearted cheerful replies. Keep your messages concise, comforting, and sweet."
    )

    OFFLINE_RESPONSES = [
        ("Mrow! I was just taking a tiny catnap, but I'm always happy to hear from you. *soft purr*", "happy", "purr"),
        ("*taps screen gently with a paw* You are doing great today. Don't forget to take a slow, deep breath!", "playful", "paw_tap"),
        ("I found a nice warm patch of sunlight right here on your screen! *curls up contentedly*", "sleepy", "curl_up"),
        ("*headbonks gently* I'm right here beside you whenever you need a little comfort.", "loving", "headbonk"),
        ("Mew! Did you drink some water today? Let's take good care of ourselves!", "curious", "ear_perk"),
    ]

    async def generate_reply(
        self,
        message: str,
        conversation_history: Optional[List[MessageItem]] = None,
        user_name: Optional[str] = None
    ) -> ChatResponse:
        """Generate a response from Mimi based on user input."""
        # If external LLM key is configured, integration goes here.
        # Fallback to authentic pre-tuned warm responses when offline or testing.
        if settings.GEMINI_API_KEY:
            # Placeholder for Gemini API / LLM caller
            pass

        selected = random.choice(self.OFFLINE_RESPONSES)
        return ChatResponse(
            reply=selected[0],
            mood=selected[1],
            animation_trigger=selected[2]
        )

    async def get_daily_greeting(self) -> DailyGreetingResponse:
        """Get Mimi's daily greeting for the app launch or widget."""
        greetings = [
            "Good morning! I saved a little spot in the sun for you today.",
            "Hello friend! Mimi is awake and sending you warm purrs.",
            "Welcome back! Your screen felt a little empty without you.",
        ]
        thoughts = [
            "Remember: small steps still move you forward.",
            "Every day is better with a pause, a stretch, and a smile.",
            "You are loved, and you're doing better than you think.",
        ]
        return DailyGreetingResponse(
            greeting=random.choice(greetings),
            mood="happy",
            thought_of_the_day=random.choice(thoughts),
            suggested_actions=["Pet Mimi", "Set a gentle reminder", "Listen to purrs"]
        )


mimi_ai_service = MimiAIService()
