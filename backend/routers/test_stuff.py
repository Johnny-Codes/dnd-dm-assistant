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
async def root():
    return {"message": "Hello World"}
