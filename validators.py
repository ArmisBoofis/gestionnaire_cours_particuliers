"""This file defines validators for some pieces of information such as
phone numbers and email addresses. These validators take the form of
functions accepting the user input and returning a boolean."""

import phonenumbers
from email_validator import validate_email, EmailNotValidError


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
