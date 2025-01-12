"""File containing the definition of the menu functions, which display
menus asking the user to make various choices and input necessay information."""

from enum import Enum
from typing import Tuple, Callable

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from student_controller import StudentController
from hourly_rate_controller import HourlyRateController
from course_controller import CourseController


def choice_menu_wrapper(menu_message: str, choices: list[Tuple[str, Callable]]) -> None:
    """Wrapper for inquirer.select ; shortcut allowing to associate functions with choices."""

    # We display the menu
    user_choice = inquirer.select(
        message=menu_message,
        choices=[Choice(i, choice[0]) for i, choice in enumerate(choices)],
    ).execute()

    # We call the corresonding action
    choices[user_choice][1]()


def students_menu() -> None:
    """Menu for student creation, edition, deletion and overview."""

    # Object used to interact with the students table inside the database
    student_controller = StudentController()

    choice_menu_wrapper(
        "Opérations disponibles pour la gestion des élèves :",
        [
            ("Créer un nouvel élève", student_controller.create_entity),
            ("Éditer un élève existant", student_controller.edit_entity),
            ("Supprimer un élève", student_controller.delete_entity),
            (
                "Consulter la liste des élèves",
                lambda: student_controller.display_entity_list(
                    message="Liste des élèves :", limit=None
                ),
            ),
        ],
    )


def courses_menu() -> None:
    """Menu for courses creation, edition, deletion and overview."""

    # Object used to interact with the hourly rates table inside the database
    courses_controller = CourseController()

    choice_menu_wrapper(
        "Opérations disponibles pour la gestion des cours :",
        [
            ("Créer un nouveau cours", courses_controller.create_entity),
            ("Éditer un cours existant", courses_controller.edit_entity),
            ("Marquer un cours existant comme payé", courses_controller.mark_as_paid),
            (
                "Marquer un cours existant comme impayé",
                courses_controller.mark_as_unpaid,
            ),
            ("Supprimer un cours", courses_controller.delete_entity),
            (
                "Consulter la liste des cours",
                lambda: courses_controller.display_entity_list(
                    message="Liste des 15 derniers cours donnés :"
                ),
            ),
        ],
    )


def houlry_rates_menu() -> None:
    """Menu for hourly rates creation, edition, deletioin and overview."""

    # Object used to interact with the hourly rates table inside the database
    hourly_rates_controller = HourlyRateController()

    choice_menu_wrapper(
        "Opérations disponibles pour la gestion des taux horaires :",
        [
            ("Créer un nouveau taux horaire", hourly_rates_controller.create_entity),
            ("Éditer un taux horaire existant", hourly_rates_controller.edit_entity),
            ("Supprimer un taux horaire", hourly_rates_controller.delete_entity),
            (
                "Consulter la liste des taux horaires",
                lambda: hourly_rates_controller.display_entity_list(
                    message="Liste des taux horaires créés :", limit=None
                ),
            ),
        ],
    )


def stats_menu() -> None:
    """Menu allowing the user to access various pieces of information
    regarding the gains he made and the debt of the students."""

    # The stats functions are implemented across the different controllers
    students_controller = StudentController()
    courses_controller = CourseController()

    choice_menu_wrapper(
        "Statistiques disponibles :",
        [
            (
                "Montants dû par les élèves",
                students_controller.display_debt_per_student,
            ),
            (
                "Gains depuis une date donnée",
                courses_controller.display_gains_since_date,
            ),
        ],
    )
