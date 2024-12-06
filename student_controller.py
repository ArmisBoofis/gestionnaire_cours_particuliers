"""This file defines the StudentManager class, used to
create, edit and delete student instances in the database"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from InquirerPy import inquirer

from models import Student
from base_controller import BaseController
from prompts import prompt_student


class StudentController(BaseController):
    """This class controls all student-related operations :
    creation, edition, deletion."""

    def create_student(self) -> None:
        """Request the information related to a new student and then
        stores the information in the database."""

        with self.session.begin() as db_session:
            student = prompt_student()
            db_session.add(student)

    def edit_student(self) -> None:
        """Asks the user for a student to edit, requests the new information,
        and reflect the changes in the database."""

        with self.session.begin() as db_session:
            # We ask the user to choose a student to edit
            chosen_student = StudentController.ask_for_student(db_session)

            # We retrieve the new information and store it in the database
            new_student = prompt_student(chosen_student)
            db_session.add(new_student)

    def delete_student(self) -> None:
        """Asks the user for a student to delete and then delete the
        corresponding row in the database."""

        with self.session.begin() as db_session:
            # We ask the user to choose a student to edit
            chosen_student = StudentController.ask_for_student(db_session)

            # We delete the corresponding student in the database
            db_session.delete(chosen_student)

    @classmethod
    def ask_for_student(cls, current_session: Session) -> Student:
        """Prints a menu asking the user to choose a student and
        returns the corresponding instance of the Student class."""

        # List of existing students
        stmt = select(Student)
        students_list = current_session.scalars(stmt)

        # Menu prompting the user to choose a student to edit
        chosen_student = inquirer.select(
            message="Quel élève voulez-vous éditer ?",
            choices=students_list,
        ).execute()

        return chosen_student
