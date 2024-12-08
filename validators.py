"""This file defines validators for some pieces of information such as
phone numbers and email addresses. These validators take the form of
functions accepting the user input and returning a boolean."""

import datetime

from decimal import Decimal, InvalidOperation
import phonenumbers
from email_validator import validate_email, EmailNotValidError

# Date format used across the app for validation and formatting
DATE_FORMAT = "%d/%m/%Y"


def validate_phone_number(raw_phone_number: str, region: str = "FR") -> bool:
    """Validates a phone number from any country in the world."""

    try:
        # We remove non-digit characters before parsing the phone number
        phone_number = phonenumbers.parse(
            "".join(filter(str.isdigit, raw_phone_number)), region
        )

        # We check if the number is possible and valid
        return phonenumbers.is_possible_number(
            phone_number
        ) and phonenumbers.is_valid_number(phone_number)

    except phonenumbers.NumberParseException:
        # The input could not even be parsed as a phone number
        return False


def validate_email_address(email_address: str) -> bool:
    """Validates an email address."""

    try:
        # The check_deliverability argument allow us to check the domain name
        email_info = validate_email(email_address, check_deliverability=True)

        # At this stage, only the length of the address can be problematic
        return len(email_info.normalized) <= 75

    except EmailNotValidError:
        return False


def validate_decimal(
    input_str: str, min_value=Decimal("0.0"), max_value=Decimal("999.99")
) -> bool:
    """Validates that the input can be represented as a float
    and that it falls in the specified range."""

    try:
        # We convert the input and check if it has a suitable value
        input_decimal = Decimal(input_str)
        return min_value <= input_decimal <= max_value

    except InvalidOperation:
        # This exception is triggered when the converion above fails
        return False


def validate_date(input_str: str, date_format=DATE_FORMAT) -> bool:
    """Function checking that a date, given as a string, follows
    the specified format."""

    try:
        datetime.datetime.strptime(input_str, date_format)
        return True

    except ValueError:
        # ValueError is raised in case the above parsing fails
        return False
