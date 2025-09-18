from fastapi import HTTPException, status, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from models.common import BearerToken

security = HTTPBearer(auto_error=True)

def get_header_authorization_bearer(
        # authorization: str = Header(..., description='Bearer token'),
        authorization: HTTPAuthorizationCredentials = Security(security)
) -> BearerToken:
    # bearerSpace: str = 'Bearer '

    # if not authorization.startswith(bearerSpace):
    #     raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             detail=f'token is required or format token is invalid.',
    #         )

    # return BearerToken(
    #     token=authorization.removeprefix(bearerSpace).strip()
    # )

    bearerSpace: str = 'Bearer'

    if not authorization.scheme == bearerSpace:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f'token is required or format token is invalid.',
            )
    
    return BearerToken(
        token=authorization.credentials.strip(),
    )