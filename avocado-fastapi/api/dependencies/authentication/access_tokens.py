from typing import TYPE_CHECKING
from fastapi import Depends

from database import AccessToken
from database.db_helper import DatabaseHelper


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
    session: "AsyncSession" = Depends(DatabaseHelper.session_getter),
):
    yield AccessToken.get_db(session=session)
