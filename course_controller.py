"""This file defines the CourseController class, used to
create, edit and delete student instances in the database."""

from models import Course
from base_controller import BaseController
from prompts import prompt_course


class CourseController(BaseController):
    """This class controls all course-related operations :
    creation, edition, deletion."""

    def __init__(self):
        super().__init__(Course, prompt_course)
