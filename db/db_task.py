from db.database import collection_tasks
from models.task import Task
from bson import ObjectId

async def get_db_tasks(key: str = '', value: any = None):
    tasks: list = []

    if key != '' and value != '':
        documents = collection_tasks.find({key: value})
    else:
        documents = collection_tasks.find({})

    async for document in documents:
        tasks.append(document)

    return tasks

async def get_db_task(id: str):
    return await get_db_one_task(key='_id', value=id)

async def create_db_task(task: Task):
    task_dict: dict = dict(task)
    if 'id' in task_dict:
        del task_dict['id']
    new_task = await collection_tasks.insert_one(task_dict)
    new_task = await collection_tasks.find_one({'_id': new_task.inserted_id, })
    return new_task

async def update_db_task(id: str, task: Task):
    task_dict: dict = dict(task)
    if '_id' in task_dict:
        del task_dict['_id']
    
    await collection_tasks.update_one({'_id': ObjectId(id),}, {'$set': task_dict})
    return await get_db_one_task(key='_id', value=id)

async def delete_db_task(id: str):
    # task: dict = {
    #     "is_deleted": True,
    # }

    # await collection_task.update_one({'_id': ObjectId(id)}, {'$set': task, })
    # return await get_db_one_task(key='_id', value=id)
    return await collection_tasks.delete_one({'_id': ObjectId(id), })
    
async def get_db_one_task(key: str, value: any):
    task: Task = Task
    if key == '_id':
        task = await collection_tasks.find_one({key: ObjectId(value)})
    else:
        task = await collection_tasks.find_one({key: value, })

    return task

async def get_db_many_tasks(filter: dict = {}):
    tasks: list= [Task]
    documents = collection_tasks.find(filter)

    async for document in documents:
        tasks.append(document)
        
    return tasks