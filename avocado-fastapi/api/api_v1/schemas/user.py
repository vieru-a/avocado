from typing import Optional

from fastapi_users import schemas

from database.types.user_id import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    first_name: str
    last_name: str
    # wish:


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    # wish:


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]
    # wish:
