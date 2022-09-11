from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.user_data.models import UserData
from application.user_data.schemas import UserDataCreate


async def create_or_update(
        session: AsyncSession, userdata: UserDataCreate
) -> bool:
    created = True
    obj = await get(session, userdata.phone_number)
    if obj is None:
        obj = UserData(**userdata.dict())
        session.add(obj)
    else:
        created = False
        for key, value in userdata.dict().items():
            setattr(obj, key, value)
    return created


async def get(session: AsyncSession, phone_number: str) -> UserData:
    res = await session.execute(
        select(UserData).where(UserData.phone_number == phone_number)
    )
    return res.scalar()


async def delete(session: AsyncSession, phone_number: str) -> bool:
    success = True
    obj = await get(session, phone_number)
    if obj is not None:
        await session.delete(obj)
    else:
        success = False
    return success

