import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from models.database import Db_settings, Db_collections

load_dotenv()

db_collections: Db_collections = Db_collections(
    tasks='tasks',
    users='users',
)
db_settings = Db_settings = Db_settings(
    url=os.getenv('MONGO_DB_URL'),
    name=os.getenv('MONGO_DB_NAME'),
    # collections=db_collections,
)

client = AsyncIOMotorClient(db_settings.url)
database = client[db_settings.name]
collection_tasks = database[db_collections.tasks]
collection_users = database[db_collections.users]

# async def get_db_tasks(key: str = '', value: any = ''):
#     tasks = []
#     if key != '' and value != '':
#         documents = collection_task.find({key: value})
#     else:
#         documents = collection_task.find({})
#     async for document in documents:
#         tasks.append(document)
#     return tasks

# async def get_db_task(id: str):
#     return await get_db_one_task(key='_id', value=id)

# async def create_db_task(task: Task):
#     task_dict: dict = dict(task)
#     if 'id' in task_dict:
#         del task_dict['id']
#     new_task = await collection_task.insert_one(task_dict)
#     new_task = await collection_task.find_one({'_id': new_task.inserted_id, })
#     return new_task

# async def update_db_task(id: str, task: Task):
#     task_dict: dict = dict(task)
#     if '_id' in task_dict:
#         del task_dict['_id']
    
#     updated_task = await collection_task.update_one({'_id': ObjectId(id),}, {'$set': task_dict})
#     return await get_db_one_task(key='_id', value=id)

# async def delete_db_task(id: str):
#     # task: dict = {
#     #     "is_deleted": True,
#     # }

#     # await collection_task.update_one({'_id': ObjectId(id)}, {'$set': task, })
#     # return await get_db_one_task(key='_id', value=id)
#     return await collection_task.delete_one({'_id': ObjectId(id), })
    
# async def get_db_one_task(key: str, value: any):
#     task: any = any
#     if key == '_id':
#         task = await collection_task.find_one({key: ObjectId(value)})
#     else:
#         task = await collection_task.find_one({key: value, })

#     return task

# async def get_db_many_tasks(filter: dict = {}):
    # tasks: list= []
    # documents = collection_task.find(filter)

    # async for document in documents:
    #     tasks.append(document)
        
    # return tasks