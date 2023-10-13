from fastapi import (
    HTTPException,
    APIRouter,
    Depends,
)
from models.npc_creation import CreateNPCIn, CreateNPCOut
from openai_api.npc_creation import npc_creation
from queries.npc_creation import NPCCreationRepo

router = APIRouter()


@router.post("/api/create_npc_character", response_model=CreateNPCOut)
async def create_npc_character(
    model: CreateNPCIn,
    repo: NPCCreationRepo = Depends(),
):
    work = model.work
    add_info = model.additional_information
    npc = npc_creation(work, add_info)
    created_npc = repo.create(npc)
    if created_npc:
        return created_npc
    else:
        raise HTTPException(status_code=500, detail="Failed to create NPC")
