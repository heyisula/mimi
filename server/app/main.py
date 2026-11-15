"""Mimi Companion API - Application Entry Point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.router import api_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend service for Mimi — a gentle, AI-powered companion living on your home screen.",
    version="0.1.0",
    debug=settings.DEBUG
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Router
app.include_router(api_router)


@app.get("/", tags=["Health"])
async def root():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "message": "Mimi is purring happily! 🐾"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
