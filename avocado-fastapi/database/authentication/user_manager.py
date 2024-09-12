import logging
from typing import Optional, TYPE_CHECKING


from fastapi_users import BaseUserManager, IntegerIDMixin

from core.config import settings
from database import User
from database.types.user_id import UserIdType

if TYPE_CHECKING:
    from fastapi import Request

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):
    reset_password_token_secret = settings.reset_password_token_secret
    verification_token_secret = settings.verification_token_secret

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has registered.",
            user.id,
        )
