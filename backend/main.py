from fastapi import FastAPI
from routers import test_stuff

app = FastAPI()

app.include_router(test_stuff.router)
