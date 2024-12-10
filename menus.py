"""File containing the definition of the different menus available
inside the app : students, courses, and rates managment among others."""

from enum import Enum, auto

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from student_controller import StudentController
from hourly_rate_controller import HourlyRateController
from course_controller import CourseController

# Enumeration of the available choices for the students menu.
StudentsMenuChoices = Enum("StudentsMenuChoices", ["CREATE", "EDIT", "DELETE", "LIST"])


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

    elif user_choice == StudentsMenuChoices.LIST:
        student_controller.display_entity_list(message="Liste des élèves :", limit=None)


# Enumeration of the available choices for the courses menu.
CoursesMenuChoices = Enum("CoursesMenuChoices", ["CREATE", "EDIT", "DELETE", "LIST"])


def courses_menu() -> None:
    """Menu for courses creation, edition, deletion and overview."""

    # We display the menu
    # We display the menu
    user_choice = inquirer.select(
        message="Opérations disponibles pour la gestion des cours :",
        choices=[
            Choice(CoursesMenuChoices.CREATE, "Créer un nouveau cours"),
            Choice(CoursesMenuChoices.EDIT, "Éditer un cours existant"),
            Choice(CoursesMenuChoices.DELETE, "Supprimer un cours"),
            Choice(CoursesMenuChoices.LIST, "Consulter la liste des cours"),
        ],
    ).execute()

    # Object used to interact with the hourly rates table inside the database
    courses_controller = CourseController()

    if user_choice == CoursesMenuChoices.CREATE:
        courses_controller.create_entity()

    elif user_choice == CoursesMenuChoices.EDIT:
        courses_controller.edit_entity()

    elif user_choice == CoursesMenuChoices.DELETE:
        courses_controller.delete_entity()

    elif user_choice == CoursesMenuChoices.LIST:
        courses_controller.display_entity_list(
            message="Liste des 15 derniers cours donnés :"
        )


# Enumeration of the available choices for the hourly rates menu.
HourlyRatesMenuChoices = Enum(
    "HourlyRatesMenuChoices", ["CREATE", "EDIT", "DELETE", "LIST"]
)


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

    elif user_choice == HourlyRatesMenuChoices.LIST:
        hourly_rates_controller.display_entity_list(
            message="Liste des taux horaires créés :", limit=None
        )


# Enumeration of the available choices for the hourly rates menu.
StatsMenuChoices = Enum("StatsMenuChoices", ["DEBT_PER_STUDENT", "GAINS_SINCE_DATE"])


def stats_menu() -> None:
    """Menu allowing the user to access various pieces of information
    regarding the gains he made and the debt of the students."""

    # We display the menu
    user_choice = inquirer.select(
        message="Statistiques disponibles",
        choices=[
            Choice(StatsMenuChoices.DEBT_PER_STUDENT, "Montants dû par les élèves"),
            Choice(StatsMenuChoices.GAINS_SINCE_DATE, "Gains depuis une date donnée"),
        ],
    ).execute()

    # The stats functions are implemented across the different controllers
    students_controller = StudentController()
    courses_controller = CourseController()

    if user_choice == StatsMenuChoices.DEBT_PER_STUDENT:
        students_controller.display_debt_per_student()

    elif user_choice == StatsMenuChoices.GAINS_SINCE_DATE:
        courses_controller.display_gains_since_date()
