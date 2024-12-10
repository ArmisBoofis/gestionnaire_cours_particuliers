"""This file defines the CourseController class, used to
create, edit and delete student instances in the database."""

import datetime
from decimal import Decimal

from InquirerPy.utils import color_print

from models import Course
from validators import DATE_FORMAT
from base_controller import BaseController
from prompts import prompt_course, prompt_date


class CourseController(BaseController):
    """This class controls all course-related operations :
    creation, edition, deletion."""

    def __init__(self):
        super().__init__(Course, prompt_course)

    def display_gains_since_date(self) -> None:
        """Displays the gains made by the user since a given date."""

        with self.session_maker.begin() as db_sesion:
            # We prompt the user for a given date (by default, the first day of the month)
            chosen_date = prompt_date(
                datetime.date.today().replace(day=1),
                prompt_message="Date à partir de laquelle les gains seront compatbilisés :",
            )

            courses_list = self._get_entity_list(db_sesion, self.model, limit=None)
            gains = Decimal(0)

            for course in courses_list:
                if course.date >= chosen_date and course.paid:
                    gains += course.duration * course.hourly_rate.price

            color_print(
                [
                    (
                        "white",
                        f"Gains réalisé depuis le {chosen_date.strftime(DATE_FORMAT)} :",
                    ),
                    ("green", f" {gains:.2f}€"),
                ]
            )
