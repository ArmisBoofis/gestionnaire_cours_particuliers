"""This file contains the description of the three models used in this small app,
using SQLAlchemy. We define the model Student, HourlyRate and Course."""

import uuid
import datetime
from typing import List
from sqlalchemy import String, DECIMAL, ForeignKey, Uuid, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class from which all the models derive."""


class Student(Base):
    """Model describing the data related to students."""

    __tablename__ = "student"

    id: Mapped[str] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)

    first_name: Mapped[str] = mapped_column(String(50))

    last_name: Mapped[str] = mapped_column(String(50))

    # We store phone numbers according to E.164 standard format
    phone_number: Mapped[str] = mapped_column(String(15))

    email_address: Mapped[str] = mapped_column(String(75))

    address: Mapped[str] = mapped_column(String(100))

    courses: Mapped[List["Course"]] = relationship(
        back_populates="student", cascade="all, delete-orphan"
    )

    def __init__(
        self, first_name="", last_name="", phone_number="", email_address="", address=""
    ):
        """Constructor override to attribure default values
        to attributes at Python-level."""

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address

    def __repr__(self) -> str:
        """Returns a description of a given student as a string."""
        return (
            f"Student(id={self.id!r}, first_name={self.first_name!r},"
            f" last_name={self.last_name!r})"
        )


class HourlyRate(Base):
    """Model describing a hourly rate associated with some kind of course."""

    __tablename__ = "hourly_rate"

    id: Mapped[str] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)

    name: Mapped[str] = mapped_column(String(50))

    # Prices up to 999.99, with two decimal places
    price: Mapped[float] = mapped_column(DECIMAL(precision=5, scale=2))

    courses: Mapped[List["Course"]] = relationship(
        back_populates="hourly_rate", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        """Returns a description of a given hourly rate as a string."""
        return f"Student(id={self.id!r}, name={self.name!r}," f" price={self.price!r})"


class Course(Base):
    """Model describing a course, given on a specific date for a specific duration."""

    __tablename__ = "course"

    id: Mapped[str] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)

    date: Mapped[datetime.date] = mapped_column(Date())

    # Duration expressed in hours
    duration: Mapped[int] = mapped_column()

    # ID of the student taking the course
    student_id: Mapped[int] = mapped_column(ForeignKey(f"{Student.__tablename__}.id"))

    student: Mapped["Student"] = relationship(back_populates="courses")

    # ID of the hourly rate associated with the course
    hourly_rate_id: Mapped[int] = mapped_column(
        ForeignKey(f"{HourlyRate.__tablename__}.id")
    )

    hourly_rate: Mapped["HourlyRate"] = relationship(back_populates="courses")

    def __repr__(self) -> str:
        return (
            f"Course(id={self.id!r}, date={self.date.strftime("%d/%m/%Y")},"
            f" duration={self.duration} hours, student_id={self.student_id})"
        )
