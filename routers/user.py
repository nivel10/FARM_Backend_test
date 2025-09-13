from fastapi import APIRouter, HTTPException, status
from schemas.user import users_register_respose_schema, user_resgister_response_schema
from models.user import User_register_response
from db.db_users import get_db_users, get_db_one_user, update_db_user

user_router = APIRouter(
    prefix='/api/users',
    tags=['users']
)

@user_router.get('/', status_code=status.HTTP_200_OK, response_model=list[User_register_response])
async def get_users():
    documents = await get_db_users()
    # documents = await get_db_tasks(key='is_deleted', value=False)
    
    return users_register_respose_schema(documents)

@user_router.put('/{id}', status_code=status.HTTP_200_OK)
async def put_user(id: str, user: User_register_response):
    user_found: User_register_response = await get_db_one_user(key='_id', value=id, key_2='', value_2=None)
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'the record is not found. Id: {id}.'
        )
    
    user.is_deleted = user_found['is_deleted']
    user.created_at = user_found['created_at']

    user_found = await update_db_user(id=id, user=user)
    
    return user_resgister_response_schema(user_found)