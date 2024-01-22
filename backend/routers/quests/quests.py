from fastapi import (
    HTTPException,
    APIRouter,
    Depends,
)
from models.quests.quests import (
    QuestIn,
    QuestOut,
    AllQuestsOut,
    UpdateQuestIn,
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
        return True
    else:
        return False


@router.get("/api/quests", response_model=AllQuestsOut)
async def get_all_quests(
    repo: QuestsRepo = Depends(),
):
    try:
        all_quests = repo.get_all_quests()
        if not all_quests:
            raise HTTPException(status_code=400, detail="No quests found")
        all_quests = AllQuestsOut(quests=all_quests)
        return all_quests
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/quests/{quest_id}", response_model=QuestOut)
async def get_quest(
    quest_id: int,
    repo: QuestsRepo = Depends(),
):
    try:
        quest = repo.get_quest(quest_id)
        if not quest:
            raise HTTPException(status_code=404, detail="Quest not found")
        return quest
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/api/quests/{quest_id}")
async def delete_quest(
    quest_id: int,
    repo: QuestsRepo = Depends(),
):
    try:
        print("Deleting quest with ID:", quest_id)
        delete_quest = repo.delete_quest(quest_id)
        if delete_quest:
            return True
        else:
            raise HTTPException(status_code=404, detail="Quest not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/api/quests/{quest_id}")
async def update_quest(
    quest_id: int,
    updated_quest: UpdateQuestIn,
    repo: QuestsRepo = Depends(),
):
    try:
        update_quest = repo.update_quest(quest_id, updated_quest)
        if update_quest:
            return update_quest
        else:
            raise HTTPException(status_code=404, detail="Quest not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
