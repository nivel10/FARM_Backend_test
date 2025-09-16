from fastapi import APIRouter, HTTPException, status
# from collections import Counter
from schemas.task import task_schema, tasks_schema
from models.task import Task
from db.db_task import get_db_tasks, get_db_task, create_db_task, get_db_one_task, update_db_task, delete_db_task, get_db_many_tasks

task_router = APIRouter(
    prefix='/api/tasks',
    tags=['tasks']
)

@task_router.get('/', response_model=list[Task])
async def get_tasks():
    documents = await get_db_tasks()
    # documents = await get_db_tasks(key='is_deleted', value=False)
    return tasks_schema(documents)

@task_router.get('/{id}', response_model=Task)
async def get_task(id: str):
    document = await get_db_task(id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'record not found. Id: {id}'
        )
    
    return task_schema(document)

@task_router.post('/', status_code=201, response_model=Task)
async def create_task(task: Task):
    task_found = await get_db_one_task(key='title', value=task.title)
    if task_found:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'the record already exists. {task.title}',
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
