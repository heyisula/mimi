"""Main API router combining all endpoint routers."""

from fastapi import APIRouter
from app.api.endpoints import companion, widget

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(companion.router)
api_router.include_router(widget.router)
