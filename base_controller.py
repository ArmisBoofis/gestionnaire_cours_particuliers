"""This file defines the BaseController class, which contains
an instance of the connection to the database. This class should
then be inherited from by controller classes."""

from typing import Type, Callable

from sqlalchemy import create_engine, select
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
        self.session_maker = sessionmaker(bind=engine)
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

    def display_entity_list(
        self,
        limit: int = 15,
        message: str = "Liste des entités pour la table {self.model.__tablename__}",
    ) -> None:
        """Displays the list of the available entites for the given model
        in the database, within the given limit."""

        # We open a new session and retrieve the list of entities
        with self.session_maker.begin() as db_session:
            entity_list = BaseController._get_entity_list(db_session, self.model, limit)

            print(message)

            for entity in entity_list:
                print(f"→ {entity}")

    @classmethod
    def _get_entity_list(cls, current_session: Session, model: Base, limit: int | None):
        """Returns a list of the entites from the given model available
        in the database."""

        # We create the query and return the result
        stmt = select(model).limit(limit) if limit is not None else select(model)
        return current_session.scalars(stmt)
