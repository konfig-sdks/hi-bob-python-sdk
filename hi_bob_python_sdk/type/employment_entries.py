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

from hi_bob_python_sdk.type.employment_entry import EmploymentEntry

class RequiredEmploymentEntries(TypedDict):
    pass

class OptionalEmploymentEntries(TypedDict, total=False):
    values: typing.List[EmploymentEntry]

class EmploymentEntries(RequiredEmploymentEntries, OptionalEmploymentEntries):
    pass
