from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, Relationship

from database import BaseModel

if TYPE_CHECKING:
    from .wish import Wish


class User(BaseModel):
    username: Mapped[str] = mapped_column(String(32), unique=True)

    wish: Mapped[list["Wish"]] = Relationship(back_populates="user")
