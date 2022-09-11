from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from application.settings import get_settings


database_url = get_settings().database_url
engine = create_async_engine(database_url, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()


async def get_db_session():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            yield session
