from fastapi import APIRouter

from api.api_v1.schemas.user import UserRead, UserCreate
from core.config import settings

from api.api_v1.fastapi_users_router import fastapi_users_router
from api.dependencies.authentication.backend import authentication_backend

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

# /login
# /logout
router.include_router(
    router=fastapi_users_router.get_auth_router(authentication_backend),
)

# /register
router.include_router(
    router=fastapi_users_router.get_register_router(UserRead, UserCreate),
)

# /request-verif-token
# /verify
router.include_router(
    router=fastapi_users_router.get_verify_router(UserRead),
)
