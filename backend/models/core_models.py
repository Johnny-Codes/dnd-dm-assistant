from pydantic import BaseModel


class BaseCharacter(BaseModel):
    name: str
    race: str
