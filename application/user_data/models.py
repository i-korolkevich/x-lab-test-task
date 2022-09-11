from datetime import datetime

from sqlalchemy import Column, DateTime, String, Integer

from application.database import Base
from application.utils.crypto import get_random_string


class UserData(Base):
    __tablename__ = 'userdata'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    patronymic = Column(String(50), nullable=True)
    phone_number = Column(String(15), nullable=False, unique=True)
    email = Column(String(320), nullable=True)
    country = Column(String(50), nullable=False)
    user_id = Column(
        String(12), nullable=False, default=lambda: get_random_string(12)
    )
    date_created = Column(DateTime, default=datetime.now, nullable=False)
    date_modified = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
