"""This file defines the StudentManager class, used to
create, edit and delete student instances in the database"""

from models import Student
from session_manager import SessionManager


class StudentManager(SessionManager):
    """Manager class for the Student model."""

    def create_student(self, student: Student) -> None:
        """Insert the given Student instance into the database."""

        with self.session.begin() as db_session:
            db_session.add(student)
