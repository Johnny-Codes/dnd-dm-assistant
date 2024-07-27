from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import npc_creation, test_stuff
from routers.quests import quests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(npc_creation.router, tags=["NPC"])
app.include_router(quests.router, tags=["Quests"])
app.include_router(test_stuff.router, tags=["Testing"])
