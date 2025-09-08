from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome():
    return {'success': True, 'message': 'Welcome to the FastAPI', }

@app.get('/api/tasks')
async def get_tasks():
    return {'success': True, 'mesaage': 'all tasks', }

@app.post('/api/tasks')
async def create_task():
    return {'success': True, 'message': 'create task', }

@app.get('/api/tasks/{id}')
async def get_task(id: str):
    return {'success': True, 'message': f'task: {id}', }

@app.put('/api/tasks/{id}')
async def update_task(id: str):
    return {'success': True, 'message': f'update task: {id}', }

@app.delete('/api/tasks/{id}')
async def delete_task(id: str):
    return {'success': True, 'message': f'delete task: {id}', }