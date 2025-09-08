import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()
db_collections: dict = {
    'tasks': 'tasks',
}
db_settings: dict = {
    'url': os.getenv('MONGO_DB_URL'),
    'name': os.getenv('MONGO_DB_NAME'),
    # 'collections': db_collections,
}

client  = AsyncIOMotorClient(db_settings['url'])
database = client[db_settings['name']]
# tasks_collection = database[db_settings['collections']['tasks']]
collection_tasks = database[db_collections['tasks']]

async def get_task(id: str):
    return await collection_tasks.find_one({'_id': id, })

async def get_tasks():
    tasks = []
    data = collection_tasks.find({})
    async for task in data:
        tasks.append(**task)
    return tasks

async def create_task(task: None):
    new_task = await collection_tasks.insert_one(task)
    created_task = await collection_tasks.find_one({'_id': new_task.inserted_id, })
    return created_task