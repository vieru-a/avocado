import asyncio
import contextlib
from os import getenv

from database import User
from database.db_helper import db_helper
from database.authentication.user_manager import UserManager

from api.api_v1.schemas.user import UserCreate
from api.dependencies.authentication.users import get_users_db
from api.dependencies.authentication.user_manager import get_user_manager

get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


default_email = getenv("DEFAULT_EMAIL", "admin@admin.com")
default_password = getenv("DEFAULT_PASSWORD", "admin")
default_is_active = True
default_is_superuser = True
default_is_verified = True
default_first_name = ""
default_last_name = ""


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
    first_name: str = default_first_name,
    last_name: str = default_last_name,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
        first_name=first_name,
        last_name=last_name,
    )
    async with db_helper.session_factory() as session:
        async with get_users_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )


if __name__ == "__main__":
    asyncio.run(create_superuser())
