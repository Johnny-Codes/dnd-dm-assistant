from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)

from dnd_api.dnd_api import get_equipment_from_api, get_weapons_from_api

router = APIRouter()


@router.get("/api/test")
async def get_equipment():
    list_of_stuff = []
    x = get_equipment_from_api()
    list_of_stuff.append(x)
    y = get_weapons_from_api()
    list_of_stuff.append(y)
    return list_of_stuff
