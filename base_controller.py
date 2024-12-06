"""This file defines the BaseController class, which contains
an instance of the connection to the database. This class should
then be inherited from by controller classes."""

from typing import Type, Callable

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from InquirerPy import inquirer

from models import Base

# Points to a sqlite file located in the root folder
DATABASE_URL = "sqlite+pysqlite:///data.db"

# The <echo> parameter toggles logging from SQL
engine = create_engine(DATABASE_URL, echo=True)


class BaseController:
    """Base class for controller classes, containing an
    instance of sessionmaker, and implementing basic operations
    on entities."""

    def __init__(self, model: Type[Base], prompt: Callable[[], Base]):
        self.session = sessionmaker(engine)
        self.model = model

        # This attribute contains a function that displays a form
        # requesting the information to the user to create the entity.
        self.prompt_entity = prompt

    def create_entity(self) -> None:
        """Request the information related to a new entity and then
        stores the information in the database."""

        with self.session.begin() as db_session:
            entity = self.prompt_entity()
            db_session.add(entity)

    def edit_entity(self) -> None:
        """Asks the user for an entity to edit, requests the new information,
        and reflect the changes in the database."""

        with self.session.begin() as db_session:
            # We ask the user to choose an entity to edit
            chosen_entity = BaseController.ask_for_entity(self.model, db_session)

            # We retrieve the new information and store it in the database
            new_entity = self.prompt_entity(chosen_entity)
            db_session.add(new_entity)

    def delete_entity(self) -> None:
        """Asks the user for an entity to delete and then delete the
        corresponding row in the database."""

        with self.session.begin() as db_session:
            # We ask the user to choose a student to edit
            chosen_student = BaseController.ask_for_entity(self.model, db_session)

            # We delete the corresponding student in the database
            db_session.delete(chosen_student)

    @classmethod
    def ask_for_entity(cls, model: Type[Base], current_session: Session) -> Base:
        """Prints a menu asking the user to choose a student and
        returns the corresponding instance of the Student class."""

        # List of existing students
        stmt = select(model)
        students_list = current_session.scalars(stmt)

        # Menu prompting the user to choose a student to edit
        chosen_student = inquirer.select(
            message="Quel élément voulez-vous éditer ?",
            choices=students_list,
        ).execute()

        return chosen_student
