from fastapi import APIRouter, status, HTTPException
from models.user import User_register, User_register_response
from db.db_users import create_db_user, get_db_one_user
from schemas.user import user_resgister_response_schema

auth_router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

@auth_router.post('/register', status_code=status.HTTP_201_CREATED, response_model=User_register_response)
async def register(user: User_register):
    user_found = await get_db_one_user(key='email', value=user.email)
    if user_found:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'the record already exists: {user.email}'
        )
    
    document = await create_db_user(user)
    return user_resgister_response_schema(document)