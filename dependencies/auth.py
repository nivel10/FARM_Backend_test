from fastapi import HTTPException, status, Header
from models.auth import BearerToken, UserPassword

def get_header_authorization_bearer(
        authorization: str = Header(..., description='Bearer token'),
):
    bearerSpace: str = 'Bearer '

    if not authorization.startswith(bearerSpace):
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f'token is required or format token is invalid.',
            )
    
    return BearerToken(
        token=authorization.removeprefix(bearerSpace).strip()
    )

def get_header_user_password(
        user_password: str = Header(..., description='User password'),
):
     if not user_password:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='password is invalid.',
        )
     
     return UserPassword(
         user_password=user_password,
     )