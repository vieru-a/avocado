from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class DataBaseConfig(BaseModel):
    database_url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 10
    max_overflow: int = 10


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DataBaseConfig


settings = Settings()