from .core_models import BaseCharacter
from pydantic import BaseModel
from typing import Optional, List


class CreateNPCIn(BaseModel):
    work: str
    additional_information: Optional[str] = None


class RolePlayingTips(BaseModel):
    id: int
    tip: str


class CreateNPCOut(BaseCharacter):
    id: int
    personality: str
    physical_description: str
    role_playing_tips: List[RolePlayingTips]


class GetOneNPC(BaseModel):
    id: int
