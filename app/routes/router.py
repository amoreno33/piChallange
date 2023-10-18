from fastapi import APIRouter
from app.routes import character_router


router = APIRouter()

router.include_router(character_router.router, 
                        prefix="/character",
                        tags=["Character"])