import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from .common.utils import *


class Base(object):
    """Created Base class model """
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )


DeclarativeBase = declarative_base(cls=Base)


class User(DeclarativeBase):
    """ This class is used to create the user information table in database """
    __tablename__ = 'users3'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    password = Column(String(90), nullable=False)
    email = Column(String(90), nullable=False)
    phone_number = Column(String(10), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)

    def __init__(self, email, password, phone_number, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.email = email_validation(email=email)
        self.phone_number = phone_number_valid(phone_number=phone_number)
        print(self.phone_number)
        self.password = password_validation_and_hashed(password=password)
