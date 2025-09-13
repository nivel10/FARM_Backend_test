from fastapi import APIRouter, HTTPException, status
from schemas.user import users_register_respose_schema
from models.user import User_register_response
from db.db_users import get_db_users

user_router = APIRouter(
    prefix='/api/users',
    tags=['users']
)

@user_router.get('/')
async def get_users():
    documents = await get_db_users()
    # documents = await get_db_tasks(key='is_deleted', value=False)
    
    return users_register_respose_schema(documents)