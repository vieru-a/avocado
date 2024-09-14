from fastapi import Depends

from database.authentication.user_manager import UserManager

from .users import get_users_db


async def get_user_manager(users_db=Depends(get_users_db)):
    yield UserManager(users_db)
