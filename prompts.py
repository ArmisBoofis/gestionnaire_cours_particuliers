"""This file contains the definition of several function prompting the user
for various pieces of information. This is done with InquirerPy and includes
validation of the data provided by the user."""

import datetime
from decimal import Decimal
from typing import Type

from sqlalchemy import select
from sqlalchemy.orm import Session
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

import validators
import sanitizers
from models import Student, HourlyRate, Course, Base


def prompt_entity_choice(
    current_session: Session,
    model: Type[Base],
    prompt_message: str = "Quelle entité voulez-vous sélectionner ?",
) -> Base:
    """Prints a menu asking the user to choose an entity and
    returns the corresponding instance of the model."""

    # List of existing entities
    stmt = select(model)
    entity_list = current_session.scalars(stmt)

    # Menu prompting the user to choose an entity
    chosen_entity = inquirer.select(
        message=prompt_message,
        choices=entity_list,
    ).execute()

    return chosen_entity


def prompt_student(_: Session, student: Student) -> None:
    """Function prompting the user to enter the data related to a student.
    The arguments can be used to specify default values for each field
    (useful when displaying the edition prompt)."""

    print("Veuillez entrer les informations relatives à l'étudiant :")

    student.first_name = inquirer.text(
        message="Prénom :",
        default=student.first_name,
        validate=lambda result: 50 >= len(result) >= 3,
        invalid_message="Le prénom doit comporter entre 3 et 50 caractères.",
    ).execute()

    student.last_name = inquirer.text(
        message="Nom :",
        default=student.last_name,
        validate=lambda result: 50 >= len(result) >= 3,
        invalid_message="Le nom doit comporter entre 3 et 50 caractères.",
    ).execute()

    # The number is transformed following E164 standard format
    student.phone_number = inquirer.text(
        message="Numéro de téléphone :",
        default=student.phone_number,
        validate=validators.validate_phone_number,
        invalid_message="Le numéro de téléphone renseigné n'est pas correct.",
        transformer=sanitizers.sanitize_phone_number,
        filter=sanitizers.sanitize_phone_number,
    ).execute()

    student.email_address = inquirer.text(
        message="Adresse email :",
        default=student.email_address,
        validate=validators.validate_email_address,
        invalid_message="Either the syntax or the domain name of the address is invalid.",
        transformer=sanitizers.sanitize_email_address,
        filter=sanitizers.sanitize_email_address,
    ).execute()

    student.address = inquirer.text(
        message="Adresse :",
        default=student.address,
    ).execute()

    # We return the modified student instance
    return student


def prompt_course(current_session: Session, course: Course):
    """Function prompting the user to enter the data related to a course.
    The arguments can be used to specify default values for each field
    (useful when displaying the edition prompt)."""

    print("Veuillez entrer les informations relatives au cours :")

    course.date = inquirer.text(
        message="Date du cours (format jj/mm/AAAA) :",
        default=course.date.strftime(validators.DATE_FORMAT),
        validate=validators.validate_date,
        invalid_message=f"La date fournie ne suit pas le format jj/mm/AAAA"
        f" (exemple : {datetime.date.today().strftime(validators.DATE_FORMAT)})",
        filter=sanitizers.sanitize_date,
    ).execute()

    course.duration = inquirer.text(
        message="Durée du cours (en heures) :",
        default=str(course.duration),
        validate=lambda res: validators.validate_decimal(
            res, min_value=Decimal("0.0"), max_value=Decimal("9.9")
        ),
        invalid_message="La durée du cours doit être comprise entre 0 et 9,9.",
        transformer=sanitizers.sanitize_decimal,
        filter=sanitizers.sanitize_decimal,
    ).execute()

    # We ask the user to choose a student and a rate to associate with this course
    course.hourly_rate = prompt_entity_choice(
        current_session, HourlyRate, prompt_message="À quel tarif correspond ce cours ?"
    )

    course.student = prompt_entity_choice(
        current_session,
        Student,
        prompt_message="À quel étudiant a été donné ce cours ?",
    )

    course.paid = inquirer.select(
        message="Ce cours a-t-il été déjà payé ?",
        choices=[Choice(True, "Oui"), Choice(False, "Non")],
    ).execute()

    return course


def prompt_hourly_rate(_: Session, hourly_rate: HourlyRate):
    """Function prompting the user to enter the data related to a hourly rate.
    The arguments can be used to specify default values for each field
    (useful when displaying the edition prompt)."""

    print("Veuillez entrer les informations relatives au taux horaire :")

    hourly_rate.name = inquirer.text(
        message="Nom du taux :",
        default=hourly_rate.name,
        validate=lambda result: 50 >= len(result) >= 3,
        invalid_message="Le nom doit comporter entre 3 et 50 caractères.",
    ).execute()

    hourly_rate.price = inquirer.text(
        message="Tarif (en euros) :",
        default=str(hourly_rate.price),
        validate=validators.validate_decimal,
        invalid_message="Le tarif horaire doit être compris entre 0€ et 999,99€.",
        transformer=sanitizers.sanitize_decimal,
        filter=sanitizers.sanitize_decimal,
    ).execute()

    return hourly_rate
