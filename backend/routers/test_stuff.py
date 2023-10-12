from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)

router = APIRouter()


@router.get("/")
async def homepage():
    return "Home"


@router.post("/api/create_npc_character")
async def create_npc_character():
    return "Hello World"
