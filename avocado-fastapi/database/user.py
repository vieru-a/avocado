from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import BaseModel


class User(BaseModel):
    username: Mapped[str] = mapped_column(String(32), unique=True)
