from fastapi import (
    HTTPException,
    APIRouter,
    Depends,
)
from models.quests.quests import (
    QuestIn,
    QuestOut,
    AllQuestsOut,
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


@router.post("/api/quests/{quest_id}/npc/{npc_id}")
async def add_npc_to_quest(
    quest_id: int,
    npc_id: int,
    repo: QuestsRepo = Depends(),
):
    add_npc_to_quest = repo.add_npc_to_quest(quest_id, npc_id)
    if add_npc_to_quest:
        return "Success"


@router.get("/api/quests", response_model=AllQuestsOut)
async def get_all_quests(
    repo: QuestsRepo = Depends(),
):
    all_quests = repo.get_all_quests()
    print("all_quests", all_quests)
    all_quests = AllQuestsOut(quests=all_quests)
    return all_quests
