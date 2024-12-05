"""File containing the definition of the different menus available
inside the app : students, courses, and rates managment among others."""

from enum import Enum

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from student_manager import StudentManager
from prompts import prompt_student


class StudentsMenuChoices(Enum):
    """Enumeration of the different choices for the students menu."""

    CREATE = 1
    EDIT = 2
    DELETE = 3
    LIST = 4


def students_menu() -> None:
    """Menu for student creation, edition, deletion and listing."""

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
    student_manager = StudentManager()

    # We perform the action corresponding to the user choice
    if user_choice == StudentsMenuChoices.CREATE:
        student = prompt_student()
        student_manager.create_student(student)
