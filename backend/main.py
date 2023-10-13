from fastapi import FastAPI
from routers import npc_creation

app = FastAPI()

app.include_router(npc_creation.router)
