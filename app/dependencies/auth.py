from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from pydantic import UUID4

from app.exceptions.custom_exception import InvalidTokenException
from app.models.data.user import User
from app.repository.user_repository import UserRepository
from app.security.security import ALGORITHM, SECRET_KEY


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], authservie: UserRepository = Depends(UserRepository)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: UUID4 = payload.get("sub")
    except jwt.InvalidTokenError:
        raise InvalidTokenException()



async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def require_role(required_role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have access to this resource",
            )
        return current_user
    return role_checker