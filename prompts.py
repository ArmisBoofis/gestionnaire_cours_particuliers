"""This file contains the definition of several function prompting the user
for various pieces of information. This is done with InquirerPy and includes
validation of the data provided by the user."""

from InquirerPy import inquirer
from validators import validate_phone_number, validate_email_address
from sanitizers import sanitize_phone_number, sanitize_email_address
from models import Student


def prompt_student(default_data=Student()) -> None:
    """Function prompting the user to enter the data related to a student.
    The arguments can be used to specify default values for each field
    (useful when displaying the edition prompt)."""

    print("Veuillez entrer les informations relatives à l'étudiant :")

    first_name = inquirer.text(
        message="Prénom :",
        default=default_data.first_name,
        validate=lambda result: 50 >= len(result) >= 3,
        invalid_message="Le prénom doit comporter entre 3 et 50 caractères.",
    ).execute()

    last_name = inquirer.text(
        message="Nom :",
        default=default_data.last_name,
        validate=lambda result: 50 >= len(result) >= 3,
        invalid_message="Le nom doit comporter entre 3 et 50 caractères.",
    ).execute()

    # The number is transformed following E164 standard format
    phone_number = inquirer.text(
        message="Numéro de téléphone :",
        default=default_data.phone_number,
        validate=validate_phone_number,
        invalid_message="Le numéro de téléphone renseigné n'est pas correct.",
        transformer=sanitize_phone_number,
        filter=sanitize_phone_number,
    ).execute()

    email_address = inquirer.text(
        message="Adresse email :",
        default=default_data.email_address,
        validate=validate_email_address,
        invalid_message="Either the syntax or the domain name of the address is invalid.",
        transformer=sanitize_email_address,
        filter=sanitize_email_address,
    ).execute()

    address = inquirer.text(
        message="Adresse :",
        default=default_data.address,
    ).execute()

    # We return a populated instance of the Student class
    return Student(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email_address=email_address,
        address=address,
    )
