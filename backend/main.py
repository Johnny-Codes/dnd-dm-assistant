from fastapi import FastAPI
from routers import npc_creation, test_stuff

app = FastAPI()

app.include_router(npc_creation.router, tags=["NPC"])
app.include_router(test_stuff.router, tags=["Testing"])
