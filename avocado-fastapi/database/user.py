from typing import TYPE_CHECKING
from fastapi_users.db import SQLAlchemyBaseUserTable

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, Relationship

from database import BaseModel
from .mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from .wish import Wish


class User(BaseModel, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    first_name: Mapped[str] = mapped_column(String(32), unique=False)
    last_name: Mapped[str] = mapped_column(String(32), unique=False)

    wish: Mapped[list["Wish"]] = Relationship(back_populates="user")
