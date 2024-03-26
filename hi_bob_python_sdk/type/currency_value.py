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


class RequiredCurrencyValue(TypedDict):
    value: typing.Union[int, float]

    # Three-letter currency code.
    currency: str

class OptionalCurrencyValue(TypedDict, total=False):
    pass

class CurrencyValue(RequiredCurrencyValue, OptionalCurrencyValue):
    pass
