# coding: utf-8

"""
    Bob API

    Access your employees data with the Bob API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from hi_bob_python_sdk.type.about_part import AboutPart
from hi_bob_python_sdk.type.personal_part import PersonalPart
from hi_bob_python_sdk.type.work_part import WorkPart

class RequiredEmployee(TypedDict):
    pass

class OptionalEmployee(TypedDict, total=False):
    # A unique identifier representing a specific employee.
    id: str

    # Employee's first name.
    firstName: str

    # Employee's surname.
    surname: str

    # Employee's email address.
    email: str

    # Employee's display name. This defaults to first name & last name but can be customized.
    displayName: str

    personal: PersonalPart

    about: AboutPart

    work: WorkPart

class Employee(RequiredEmployee, OptionalEmployee):
    pass