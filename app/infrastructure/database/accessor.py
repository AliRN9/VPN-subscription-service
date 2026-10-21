from collections.abc import AsyncGenerator

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.settings import settings


class DatabaseAccessor:
    def __init__(
        self,
        db_url: str | URL,
        echo: bool = False,
        pool_pre_ping: bool = True,
        echo_pool: bool = False,
        pool_size: int = 5,
        max_overflow: int = 10,
    ) -> None:
        self.engine = create_async_engine(
            url=db_url,
            echo=echo,
            pool_pre_ping=pool_pre_ping,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )

        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_accessor = DatabaseAccessor(
    db_url=settings.database.url,
    echo=False,
    pool_pre_ping=True,
    echo_pool=False,
    pool_size=10,
    max_overflow=8,
)
