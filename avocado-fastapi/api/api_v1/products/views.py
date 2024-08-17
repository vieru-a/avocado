from typing import Annotated

from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_helper import db_helper
from . import crud
from .dependencies import product_by_id
from .schemas import Product, ProductCreate, ProductUpdatePartial

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    product_in: ProductCreate,
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}", response_model=Product)
async def get_product_by_id(product: Product = Depends(product_by_id)):
    return product


@router.patch("/{product_id}", response_model=Product)
async def update_product(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud.update_product_partial(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    return await crud.delete_product(session=session, product=product)
