from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import BaseModel


class Wish(BaseModel):
    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default=None,
        server_default=None,
    )
    holiday: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
