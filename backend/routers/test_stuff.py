from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)

router = APIRouter()


@router.post("/api/create_npc_character")
async def create_npc_character():
    pass
