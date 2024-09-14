from fastapi_users import FastAPIUsers

from database import User
from database.types.user_id import UserIdType

from api.dependencies.authentication.backend import authentication_backend
from api.dependencies.authentication.user_manager import get_user_manager

fastapi_users_router = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
