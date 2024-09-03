from typing import TYPE_CHECKING
from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, Relationship

from database import BaseModel
from .mixins.id_int_pk import IdIntPkMixin
from .types.user_id import UserIdType

if TYPE_CHECKING:
    from .wish import Wish
    from sqlalchemy.ext.asyncio import AsyncSession


class User(BaseModel, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    first_name: Mapped[str] = mapped_column(String(32), unique=False)
    last_name: Mapped[str] = mapped_column(String(32), unique=False)

    wish: Mapped[list["Wish"]] = Relationship(back_populates="user")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
