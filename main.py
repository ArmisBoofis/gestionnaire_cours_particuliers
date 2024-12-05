"""Main script of the tool, orchestrating the different parts of the app,
all implemented in different files."""

from enum import Enum

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

# Points to a sqlite file located in the root folder
DATABASE_URL = "sqlite+pysqlite:///data.db"


class MainMenuChoices(Enum):
    """Enumeration of the different choices for the main menu"""

    COURSES = 1
    STUDENTS = 2
    RATES = 3
    QUIT_APP = 4


if __name__ == "__main__":
    # The <echo> parameter toggles logging from SQL
    engine = create_engine(DATABASE_URL, echo=True)

    # We open a SQL session
    with Session(engine) as db_session:
        print("Bienvenue dans le gestionnaire de cours particuliers.")

        current_choice = MainMenuChoices.COURSES

        # Application loop
        while current_choice != MainMenuChoices.QUIT_APP:
            # We display the main menu
            current_choice = inquirer.select(
                message="Quelle action souhaitez-vous effectuer ?",
                choices=[
                    Choice(MainMenuChoices.COURSES, "Gérer les cours"),
                    Choice(MainMenuChoices.STUDENTS, "Gérer les élèves"),
                    Choice(MainMenuChoices.QUIT_APP, "Quitter le gestionnaire"),
                ],
            ).execute()

        print("On se revoit prochainement pour des aventures de folie !")
