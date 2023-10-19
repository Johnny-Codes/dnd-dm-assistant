from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)

from dnd_api.dnd_api import get_equipment_from_api

router = APIRouter()


@router.get("/api/test")
async def get_equipment():
    x = get_equipment_from_api()
    return x
