from typing import TYPE_CHECKING
from fastapi import Depends

from database import User
from database.db_helper import DatabaseHelper


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(
    session: "AsyncSession" = Depends(DatabaseHelper.session_getter),
):
    yield User.get_db(session=session)
