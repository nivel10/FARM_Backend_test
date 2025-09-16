from fastapi import APIRouter, status, HTTPException
from models.user import UserRegister, UserRegisterResponse, UserLogin
from db.db_users import create_db_user, get_db_one_user
from schemas.user import user_resgister_response_schema

auth_router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

@auth_router.post('/register', status_code=status.HTTP_201_CREATED, response_model=UserRegisterResponse)
async def register(user: UserRegister):
    user_found = await get_db_one_user(key='email', value=user.email, key_2='', value_2=None)
    if user_found:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'the record already exists: {user.email}'
        )
    
    document = await create_db_user(user)
    return user_resgister_response_schema(document)

@auth_router.post('/login', status_code=status.HTTP_200_OK, response_model=UserRegisterResponse)
async def login(data: UserLogin):
    user_found = await get_db_one_user(key='email', value=data.email, key_2='password', value_2=data.password)
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='email or password incorrect',
        )
    
    return user_resgister_response_schema(user_found)