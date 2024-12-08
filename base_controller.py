"""This file defines the BaseController class, which contains
an instance of the connection to the database. This class should
then be inherited from by controller classes."""

from typing import Type, Callable, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models import Base
from prompts import prompt_entity_choice

# Points to a sqlite file located in the root folder
DATABASE_URL = "sqlite+pysqlite:///data.db"

# The <echo> parameter toggles logging from SQL
engine = create_engine(DATABASE_URL, echo=False)


class BaseController:
    """Base class for controller classes, containing an
    instance of sessionmaker, and implementing basic operations
    on entities."""

    def __init__(self, model: Type[Base], prompt: Callable[[Session, Base], Base]):
        self.session_maker = sessionmaker(engine)
        self.model = model

        # This attribute contains a function that displays a form
        # requesting the information to the user to create the entity.
        self.prompt_entity = prompt

    def create_entity(self) -> None:
        """Request the information related to a new entity and then
        stores the information in the database."""

        with self.session_maker.begin() as db_session:
            # We create a void entity
            entity = self.model()

            # The prompt function changes the entity according to the user choices
            self.prompt_entity(db_session, entity)
            db_session.add(entity)

    def edit_entity(
        self, prompt_message: str = "Quelle entité voulez-vous modifier ?"
    ) -> None:
        """Asks the user for an entity to edit, requests the new information,
        and reflect the changes in the database."""

        with self.session_maker.begin() as db_session:
            # We ask the user to choose an entity to edit
            chosen_entity = prompt_entity_choice(db_session, self.model, prompt_message)

            # The prompt function changes the entity according to the user choices
            self.prompt_entity(db_session, chosen_entity)

    def delete_entity(
        self, prompt_message: str = "Quelle entité voulez-vous supprimer ?"
    ) -> None:
        """Asks the user for an entity to delete and then delete the
        corresponding row in the database."""

        with self.session_maker.begin() as db_session:
            # We ask the user to choose an entity to delete
            chosen_entity = prompt_entity_choice(db_session, self.model, prompt_message)

            # We delete the corresponding entity in the database
            db_session.delete(chosen_entity)
