import pytest
from httpx import AsyncClient
from starlette import status

from application.main import app
from application.user_data import schemas


@pytest.mark.asyncio
async def test_create():
    data = schemas.UserDataCreate(
        name='Иван',
        surname='Королькевич',
        patronymic='Владимирович',
        email='ikorolkevich@gmail.com',
        country='Россия',
        phone_number='7-904-505-01-29'
    )
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/save_user_data", json=data.dict())
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_update():
    data = schemas.UserDataCreate(
        name='Надежда',
        surname='Петрова',
        patronymic='Ивановна',
        email='nadezda@mail.ru',
        country='Казахстан',
        phone_number='7-904-505-01-29'
    )
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/save_user_data", json=data.dict())
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_update_invalid_entity():
    data = dict(
        name='Надежда1',
        surname='Петрова1',
        patronymic='Ивановна1',
        email='nadezda@mailru',
        country='Казахстан1',
        phone_number='7-904-505-01-29'
    )
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/save_user_data", json=data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_get():
    data = schemas.UserDataGet(
        phone_number='7-904-505-01-29'
    )
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/get_user_data", json=data.dict())
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_delete():
    data = schemas.UserDataGet(
        phone_number='7-904-505-01-29'
    )
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/delete_user_data", json=data.dict())
    assert response.status_code == status.HTTP_200_OK
