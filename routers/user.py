from fastapi import APIRouter, HTTPException, status, Depends
from schemas.user import users_register_respose_schema, user_resgister_response_schema
from models.user import UserRegisterResponse, User
from models.auth import BearerToken, UserPassword
from db.db_users import get_db_users, get_db_one_user, update_db_user, delete_db_user
from dependencies.auth import get_header_authorization_bearer, get_header_user_password

user_router = APIRouter(
    prefix='/api/users',
    tags=['users']
)

@user_router.get('/', status_code=status.HTTP_200_OK, response_model=list[User])
async def get_users():
    documents = await get_db_users()
    # documents = await get_db_tasks(key='is_deleted', value=False)
    
    return users_register_respose_schema(documents)

@user_router.put('/{id}', status_code=status.HTTP_200_OK, response_model=UserRegisterResponse)
async def put_user(id: str, user: UserRegisterResponse):
    user_found: UserRegisterResponse = await get_db_one_user(key='_id', value=id, key_2='', value_2=None)
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'the record is not found. Id: {id}.'
        )
    
    user.is_deleted = user_found['is_deleted']
    user.created_at = user_found['created_at']

    user_found = await update_db_user(id=id, user=user)
    
    return user_resgister_response_schema(user_found)

@user_router.delete('/{id}', status_code=status.HTTP_200_OK, response_model=UserRegisterResponse)
async def delete_user(
    id: str,
    token_header: BearerToken = Depends(get_header_authorization_bearer),
    user_password: UserPassword = Depends(get_header_user_password),
):
    user_found: User = await get_db_one_user(key='_id', value=id)
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'the record is not found. Id: {id}',
        )

    if not user_found['password'] == user_password.user_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='password incorrect',
        )
    
    result = await delete_db_user(id=id)
    if result.deleted_count <= 0 or not result.acknowledged:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'record not found. Id: {id}',
        )
    
    return user_resgister_response_schema(user_found)