from fastapi import FastAPI
from routers.task import task_router
from routers.auth import auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='FARM - test',
    version='1.0.0',
    description='This is an example from FARM (Fast API / React JS / Mongo DB)',
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(task_router)
app.include_router(auth_router)