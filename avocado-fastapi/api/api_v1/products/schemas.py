from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    category: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdatePartial(ProductCreate):
    name: str | None = None
    description: str | None = None
    category: str | None = None
    price: int | None = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
