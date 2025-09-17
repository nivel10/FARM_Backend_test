from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
# from collections import Counter
from schemas.task import task_schema, tasks_schema
from models.task import Task
from db.db_task import get_db_tasks, get_db_task, create_db_task, get_db_one_task, update_db_task, delete_db_task, get_db_many_tasks

task_router = APIRouter(
    prefix='/api/tasks',
    tags=['tasks']
)

@task_router.get('/', status_code=status.HTTP_200_OK, response_model=list[Task])
async def get_tasks():
    documents = await get_db_tasks()
    # documents = await get_db_tasks(key='is_deleted', value=False)
    return tasks_schema(documents)

@task_router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Task)
async def get_task(id: str):
    document = await get_db_task(id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'record not found. Id: {id}'
        )
    
    return task_schema(document)

@task_router.get('/{id}/{user_id}', status_code=status.HTTP_200_OK)
async def get_task_id_userId(id: str, user_id: str):
    filter: dict = {
        '_id': ObjectId(id),
        'created_by': ObjectId(user_id),
    }
    task_found = await get_db_many_tasks(filter=filter)
    print(task_found)
    if not task_found or len(task_found) <= 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'record not foud. Id: {id}; user: {user_id}',
        )
    return len(task_found)

@task_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Task)
async def create_task(task: Task):
    # task_found = await get_db_one_task(key='title', value=task.title)
    # if task_found:
    #     raise HTTPException(
    #         status_code=status.HTTP_409_CONFLICT,
    #         detail=f'the record already exists. {task.title}',
    #     )
    
    if not ObjectId.is_valid(task.created_by):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f'created by is not valid. {task.created_by}',
        )
    
    filter: dict = {
        'title': task.title,
        'created_by': ObjectId(task.created_by),
    }
    
    task_found = await get_db_many_tasks(filter=filter)
    if task_found or len(task_found) > 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'the record already exists. {task.title}',
        )

    user_found = await get_db_one_task(key='_id', value=task.created_by)
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'record not found. created by: {task.created_by}',
        )
    
    document = await create_db_task(task)
    return task_schema(document)

@task_router.put('/{id}', response_model=Task)
async def update_task(id: str, task: Task):
    tasks_found = await get_db_many_tasks({'title': task.title, 'is_deleted': False, })
    if tasks_found:
        tasks_found = tasks_schema(tasks_found)
        leakeds = [obj['title'] for obj in tasks_found if obj['id'] != id]
        # counter = Counter(leakeds)
        if len(leakeds) > 0:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'the record already exists. {task.title}',
            )
    
    updated_task = await update_db_task(id=id, task=task)

    return task_schema(updated_task)

@task_router.delete('/{id}', response_model=Task)
async def delete_task(id: str):
    task_found = await get_db_one_task(key='_id', value=id)
    if not task_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'record not found. Id: {id}',
        )
    
    # return await delete_db_task(id)
    result = await delete_db_task(id)
    if result.deleted_count <= 0 or not result.acknowledged:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'record not found. Id: {id}',
        )
    
    return task_schema(task_found)
