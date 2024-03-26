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


class RequiredPersonalPart(TypedDict):
    pass

class OptionalPersonalPart(TypedDict, total=False):
    # The employee's title, This can be Mr, Mrs. Ms. etc.
    honorific: str

    shortBirthDate: str

    # One of Male / Female.
    gender: str

class PersonalPart(RequiredPersonalPart, OptionalPersonalPart):
    pass
