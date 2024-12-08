"""Main script of the tool, orchestrating the different parts of the app,
all implemented in different files."""

from enum import Enum

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from menus import students_menu, houlry_rates_menu, courses_menu


class MainMenuChoices(Enum):
    """Enumeration of the different choices for the main menu"""

    COURSES = 1
    STUDENTS = 2
    RATES = 3
    QUIT_APP = 4
    HOURLY_RATES = 5


if __name__ == "__main__":
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
                Choice(MainMenuChoices.HOURLY_RATES, "Gérer les taux horaire"),
                Choice(MainMenuChoices.QUIT_APP, "Quitter le gestionnaire"),
            ],
        ).execute()

        # We display the sub-menu corresponding to the user choice
        if current_choice == MainMenuChoices.STUDENTS:
            students_menu()

        elif current_choice == MainMenuChoices.COURSES:
            courses_menu()

        elif current_choice == MainMenuChoices.HOURLY_RATES:
            houlry_rates_menu()

    print("On se revoit prochainement pour des aventures de folie !")
