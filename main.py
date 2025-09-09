from fastapi import FastAPI
from routers.task import task_router

app = FastAPI()

app.include_router(task_router)