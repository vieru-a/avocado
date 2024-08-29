from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import BaseModel
from database.mixins.id_int_pk import IdIntPkMixin


class Product(BaseModel, IdIntPkMixin):
    title: Mapped[str] = mapped_column(String(100), unique=False)
    description: Mapped[str] = mapped_column(
        Text,
        default=None,
        server_default=None,
    )
    price: Mapped[int]
