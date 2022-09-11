from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, constr


Cyrillic50CharsType = constr(max_length=50, regex=r'^[а-яА-Я -]+$')


class UserDataGet(BaseModel):
    phone_number: constr(max_length=15, regex=r'^7-\d{3}-\d{3}-\d{2}-\d{2}$')

    class Config:
        schema_extra = {
            'example': {
                'phone_number': '7-908-111-22-33',
            }
        }


class UserDataCreate(UserDataGet):
    name: Cyrillic50CharsType
    surname: Cyrillic50CharsType
    patronymic: Optional[Cyrillic50CharsType]
    email: Optional[EmailStr]
    country: Cyrillic50CharsType

    class Config:
        schema_extra = {
            'example': {
                'name': 'Иван',
                'surname': 'Иванов',
                'patronymic': 'Иванович',
                'email': 'ivanovivan@abc.com',
                'country': 'Россия',
                'phone_number': '7-908-111-22-33',
            }
        }


class UserDataExtended(UserDataCreate):
    country_code: str

    class Config:
        schema_extra = {
            'example': {
                'country_code': 123,
            }
        }


class UserDataDB(UserDataCreate):
    user_id: constr(max_length=12)
    date_created: datetime
    date_modified: datetime

    class Config:
        orm_mode = True


class UserDataResponse(BaseModel):
    message: str
