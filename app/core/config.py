from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "FastAPI Project"
    version: str = "0.1.0"
    debug: bool = False

    # Database
    database_url: Optional[str] = None

    # Security
    secret_key: str = Field(default="defaultsecret", env="SECRET_KEY")
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
