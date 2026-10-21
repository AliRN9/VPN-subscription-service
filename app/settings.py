from typing import Literal

from pydantic import BaseModel, SecretStr,HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

class AppConfig(BaseModel):
    title: str = "Subscription Service"
    version: str = "0.1"
    host: str = "0.0.0.0"
    port: int = 8000
    cors_origins: list[str] = ["*"]

    environment: Literal["local", "production"] = "local"

class DatabaseConfig(BaseModel):

    host: str
    port: int = 5432
    user: str
    password: SecretStr
    db: str
    driver: str = "postgresql+asyncpg"

    @property
    def url(self) -> URL:
        return URL.create(
            drivername=self.driver,
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.db,
        )


class RemnawaveConfig(BaseModel):

    url: HttpUrl
    token: SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )
    app: AppConfig = AppConfig()
    database: DatabaseConfig
    remnawave: RemnawaveConfig


settings = Settings()
