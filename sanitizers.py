"""This file contains the sanitizers used in the app, i.e the functions
applied to the data provided by the user after he typed it. This is
used to have consistent data formatting inside the database."""

import phonenumbers
from email_validator import validate_email


def sanitize_phone_number(raw_phone_number: str, region: str = "FR") -> str:
    """Puts a raw phone number into E.164 standard format."""

    # We strip the number from non-digit characters
    # Then we instanciate a phonenumbers object
    phone_number = phonenumbers.parse(
        "".join(filter(str.isdigit, raw_phone_number)), region
    )

    return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)


def sanitize_email_address(raw_email_address: str) -> str:
    """Transforms a raw email address into a standard format."""

    # We do not check deliverability as it has been done before at this stage
    email_info = validate_email(raw_email_address, check_deliverability=False)

    return email_info.normalized
