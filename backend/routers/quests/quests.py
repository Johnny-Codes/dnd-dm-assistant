from fastapi import (
    HTTPException,
    APIRouter,
    Depends,
)
from models.quests.quests import (
    QuestIn,
    QuestOut,
)
from queries.quests.quests import QuestsRepo

router = APIRouter()


@router.post("/api/quests", response_model=QuestOut)
async def create_quest(
    model: QuestIn,
    repo: QuestsRepo = Depends(),
):
    create_quest = repo.create_quest(model)
    if create_quest:
        return create_quest
    elif create_quest is False:
        raise HTTPException(status_code=500, detail="Failed to create quest")
    else:
        raise HTTPException(status_code=400, detail="Bad request")


@router.post("/api/{quest_id}/npcs", response_model=QuestOut)
async def add_npc_to_quest():
    pass
