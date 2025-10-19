import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/mohl",
)

engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)  # ← remove async_fallback
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase): ...
async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
