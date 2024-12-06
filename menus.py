"""File containing the definition of the different menus available
inside the app : students, courses, and rates managment among others."""

from enum import Enum

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from student_controller import StudentController
from hourly_rate_controller import HourlyRateController


class StudentsMenuChoices(Enum):
    """Enumeration of the available choices for the students menu."""

    CREATE = 1
    EDIT = 2
    DELETE = 3
    LIST = 4


def students_menu() -> None:
    """Menu for student creation, edition, deletion and overview."""

    # We display the menu
    user_choice = inquirer.select(
        message="Opérations disponibles pour la gestion des élèves :",
        choices=[
            Choice(StudentsMenuChoices.CREATE, "Créer un nouvel élève"),
            Choice(StudentsMenuChoices.EDIT, "Éditer un élève existant"),
            Choice(StudentsMenuChoices.DELETE, "Supprimer un élève"),
            Choice(StudentsMenuChoices.LIST, "Consulter la liste des élèves"),
        ],
    ).execute()

    # Object used to interact with the students table inside the database
    student_controller = StudentController()

    # We perform the action corresponding to the user choice
    if user_choice == StudentsMenuChoices.CREATE:
        student_controller.create_entity()

    elif user_choice == StudentsMenuChoices.EDIT:
        student_controller.edit_entity()

    elif user_choice == StudentsMenuChoices.DELETE:
        student_controller.delete_entity()


class HourlyRatesMenuChoices(Enum):
    """Enumeration of the available choices for the hourly rates menu."""

    CREATE = 1
    EDIT = 2
    DELETE = 3
    LIST = 4


def houlry_rates_menu() -> None:
    """Menu for hourly rates creation, edition, deletioin and overview."""

    # We display the menu
    user_choice = inquirer.select(
        message="Opérations disponibles pour la gestion des taux horaires :",
        choices=[
            Choice(HourlyRatesMenuChoices.CREATE, "Créer un nouveau taux horaire"),
            Choice(HourlyRatesMenuChoices.EDIT, "Éditer un taux horaire existant"),
            Choice(HourlyRatesMenuChoices.DELETE, "Supprimer un taux horaire"),
            Choice(HourlyRatesMenuChoices.LIST, "Consulter la liste des taux horaires"),
        ],
    ).execute()

    # Object used to interact with the hourly rates table inside the database
    hourly_rates_controller = HourlyRateController()

    if user_choice == HourlyRatesMenuChoices.CREATE:
        hourly_rates_controller.create_entity()

    elif user_choice == HourlyRatesMenuChoices.EDIT:
        hourly_rates_controller.edit_entity()

    elif user_choice == HourlyRatesMenuChoices.DELETE:
        hourly_rates_controller.delete_entity()
