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


class RequiredError(TypedDict):
    pass

class OptionalError(TypedDict, total=False):
    # The unique identifier of the error.
    key: str

    # A human readable error message.
    error: str

class Error(RequiredError, OptionalError):
    pass
