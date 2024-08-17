from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper, Product
from . import crud


async def product_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.db_helper.session_getter)],
    product_id: int,
) -> Product:
    product = await crud.get_product_by_id(session=session, product_id=product_id)
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found",
    )
