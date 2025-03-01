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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from hi_bob_python_sdk.pydantic.about_part import AboutPart
from hi_bob_python_sdk.pydantic.personal_part import PersonalPart
from hi_bob_python_sdk.pydantic.work_part import WorkPart

class Employee(BaseModel):
    # A unique identifier representing a specific employee.
    id: typing.Optional[str] = Field(None, alias='id')

    # Employee's first name.
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # Employee's surname.
    surname: typing.Optional[str] = Field(None, alias='surname')

    # Employee's email address.
    email: typing.Optional[str] = Field(None, alias='email')

    # Employee's display name. This defaults to first name & last name but can be customized.
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    personal: typing.Optional[PersonalPart] = Field(None, alias='personal')

    about: typing.Optional[AboutPart] = Field(None, alias='about')

    work: typing.Optional[WorkPart] = Field(None, alias='work')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
