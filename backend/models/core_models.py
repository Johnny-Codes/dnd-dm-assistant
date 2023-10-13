from pydantic import BaseModel
from typing import Optional


class BaseCharacter(BaseModel):
    name: str
    race: str
