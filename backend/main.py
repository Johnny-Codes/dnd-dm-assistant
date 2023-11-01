from fastapi import FastAPI
from routers import npc_creation, test_stuff
from routers.quests import quests

app = FastAPI()

app.include_router(npc_creation.router, tags=["NPC"])
app.include_router(quests.router, tags=["Quests"])
app.include_router(test_stuff.router, tags=["Testing"])
