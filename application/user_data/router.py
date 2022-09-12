from fastapi import APIRouter, status, Depends, HTTPException

from application.database import get_db_session
from application.redis import get_redis
from application.settings import get_settings
from application.user_data import crud
from application.user_data.schemas import (
    UserDataResponse, UserDataExtended, UserDataCreate, UserDataGet, UserDataDB
)
from application.utils.dadata import get_country_code


cache_lifetime = get_settings().cache_lifetime_sec
router = APIRouter()


@router.post('/save_user_data', status_code=status.HTTP_201_CREATED)
async def save_user_data(
        data: UserDataCreate,
        db_session=Depends(get_db_session)
) -> UserDataResponse:
    created = await crud.create_or_update(db_session, data)
    msg = 'created' if created else 'updated'
    return UserDataResponse(message=msg)


@router.post('/get_user_data', status_code=status.HTTP_200_OK)
async def get_user_data(
        data: UserDataGet,
        db_session=Depends(get_db_session),
        cache=Depends(get_redis)
) -> UserDataExtended:
    user_data = await crud.get(db_session, data.phone_number)
    if user_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    cache_key = user_data.country.lower()
    country_code = await cache.get(cache_key)
    if country_code is None:
        country_code = await get_country_code(user_data.country)
        await cache.set(cache_key, country_code, ex=cache_lifetime)
    return UserDataExtended(
        **UserDataDB.from_orm(user_data).dict(),
        country_code=country_code
    )


@router.post('/delete_user_data', status_code=status.HTTP_200_OK)
async def delete_user_data(
        data: UserDataGet,
        db_session=Depends(get_db_session)
) -> UserDataResponse:
    deleted = await crud.delete(db_session, data.phone_number)
    msg = 'deleted' if deleted else 'not found'
    return UserDataResponse(message=msg)
