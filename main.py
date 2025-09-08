from fastapi import FastAPI
from typing import Union
from models.item import Item

app = FastAPI()

@app.get('/')
async def welcome():
    return {'success': True, 'message': 'Welcome to the FastAPI', }

@app.get('/items/{id}')
async def read_items(id: int, q: Union[str, None] = None):
    return {'success': True, 'data': {'id': id, 'q': q,}, }

@app.put('/items/{id}')
async def update_item(id: int, item: Item):
    return {'success': True, 'data': {'id': id, 'name': item.name, }, }