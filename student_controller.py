"""This file defines the StudentController class, used to
create, edit and delete student instances in the database"""

from base_controller import BaseController

from models import Student
from prompts import prompt_student


class StudentController(BaseController):
    """This class controls all student-related operations :
    creation, edition, deletion."""

    def __init__(self):
        super().__init__(Student, prompt_student)
