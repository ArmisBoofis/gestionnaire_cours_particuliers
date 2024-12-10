"""This file defines the StudentController class, used to
create, edit and delete student instances in the database"""

from decimal import Decimal

from InquirerPy.utils import color_print

from base_controller import BaseController
from prompts import prompt_student
from models import Student


class StudentController(BaseController):
    """This class controls all student-related operations :
    creation, edition, deletion."""

    def __init__(self):
        super().__init__(Student, prompt_student)

    def display_debt_per_student(self) -> None:
        """Print a list of every student with associated debts."""

        with self.session_maker.begin() as db_session:
            # We first retrieve the list of the students
            students_list = BaseController._get_entity_list(
                db_session, self.model, None
            )

            for student in students_list:
                debt = Decimal(0)

                for course in student.courses:
                    if not course.paid:
                        debt += course.hourly_rate.price * course.duration

                color_print(
                    [
                        ("white", f"→ {student} - "),
                        (
                            "green" if debt == Decimal(0) else "red",
                            f"Dette : {debt:.2f}€",
                        ),
                    ]
                )
