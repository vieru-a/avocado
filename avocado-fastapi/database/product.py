from sqlalchemy.orm import Mapped

from database import BaseModel


class Product(BaseModel):

    name: Mapped[str]
    description: Mapped[str]
    category: Mapped[str]
    price: Mapped[int]
