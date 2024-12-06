"""This file defines the HourlyRateController class, used to
create, edit and delete student instances in the database"""

from base_controller import BaseController

from models import HourlyRate
from prompts import prompt_hourly_rate


class HourlyRateController(BaseController):
    """This class controls all hourly rate-related operations :
    creation, edition, deletion."""

    def __init__(self):
        super().__init__(HourlyRate, prompt_hourly_rate)
