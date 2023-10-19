from fastapi import (
    HTTPException,
    APIRouter,
    Depends,
)
from models.npc_creation import (
    CreateNPCIn,
    CreateNPCOut,
)
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


@router.get("/api/get_all_npc_level_one_characters")
async def get_all_npc_level_one_characters(
    repo: NPCCreationRepo = Depends(),
):
    all_npcs = repo.get_all_npc_level_one_chars()
    return all_npcs


@router.get("/api/get_npc_level_one/{npc_id}", response_model=CreateNPCOut)
async def get_npc_level_one(
    npc_id: int,
    repo: NPCCreationRepo = Depends(),
):
    npc = repo.get_npc_level_one(npc_id)
    return npc
