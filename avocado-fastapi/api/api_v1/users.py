from fastapi import APIRouter

from api.api_v1.schemas.user import UserRead, UserUpdate
from core.config import settings

from api.api_v1.fastapi_users_router import fastapi_users_router

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)

# /me
# /{id}
router.include_router(
    router=fastapi_users_router.get_users_router(UserRead, UserUpdate),
)
