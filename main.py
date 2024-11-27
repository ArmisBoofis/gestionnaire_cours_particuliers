"""Main script of the tool, orchestrating the different parts of the app,
all implemented in different files."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Points to a sqlite file located in the root folder
DATABASE_URL = "sqlite+pysqlite:///data.db"

if __name__ == "__main__":
    # The <echo> parameter toggles logging from SQL
    engine = create_engine(DATABASE_URL, echo=True)

    # We open a SQL session
    with Session(engine) as db_session:
        print("Session :", db_session)
