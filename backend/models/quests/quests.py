from pydantic import BaseModel
from typing import List, Optional
from models.npc_creation import CreateNPCOut


class QuestIn(BaseModel):
    name: str
    description: Optional[str] = None


class QuestOut(QuestIn):
    id: int
    npcs: Optional[List[CreateNPCOut]] = None


class AllQuestsOut(BaseModel):
    quests: List[QuestOut]
