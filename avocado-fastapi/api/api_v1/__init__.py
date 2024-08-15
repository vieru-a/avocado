from fastapi import APIRouter

from core.config import settings
from .products.views import router as products_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(router=products_router, prefix=settings.api.v1.products)
