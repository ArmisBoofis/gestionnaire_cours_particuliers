"""This file defines the SessionManager class, which contains
an instance of the connection to the database. This class should
then be inherited from by controller classes."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Points to a sqlite file located in the root folder
DATABASE_URL = "sqlite+pysqlite:///data.db"

# The <echo> parameter toggles logging from SQL
engine = create_engine(DATABASE_URL, echo=True)


class SessionManager:
    """Base class for controller classes, containing an
    instance of sessionmaker, to connect to the database."""

    def __init__(self):
        self.session = sessionmaker(engine)
