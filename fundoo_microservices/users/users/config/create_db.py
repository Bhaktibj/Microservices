# import lib
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import warnings

pymysql.install_as_MySQLdb()
from ..models import DeclarativeBase
from ...settings import MYSQL_DB_CONFIG


class DatabaseService:
    """ this method is used to create the session"""

    @staticmethod
    def db_connection():
        try:
            with warnings.catch_warnings():  # with warnings
                warnings.simplefilter('ignore')  # if warning just ignore that
                try:
                    db_engine = create_engine(
                        'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'.format(**MYSQL_DB_CONFIG))
                    db_engine.execute(
                        "CREATE DATABASE IF NOT EXISTS {} ".format(MYSQL_DB_CONFIG.get("db_name")))  # create the engine
                    print("=================>mysql database connected: {}".format(db_engine))
                    DeclarativeBase.metadata.create_all(db_engine)  # create all engine
                    if db_engine:  # if db_engine
                        Session = sessionmaker()  # create session using sessionmaker() lib
                        Session.configure(bind=db_engine)  # configure engine
                        session = Session()
                    return session  # return session object
                except ConnectionError:
                    raise Exception("connection error")
        except KeyError:
            print("key error")
