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


class RequiredBalanceResult(TypedDict):
    pass

class OptionalBalanceResult(TypedDict, total=False):
    # Employee ID.
    employeeId: str

    # The retrieved balance as of this date.
    totalBalanceAsOfDate: typing.Union[int, float]

    # The retrieved rounded balance as of this date.
    totalRoundedBalanceAsOfDate: typing.Union[int, float]

    # The balance date.
    pointInTime: date

    # The balance as of the cycle start date.
    startingBalance: typing.Union[int, float]

    # The cycle start date.
    startingBalanceAsOf: date

    # Total number of days/hours taken.
    totalTaken: typing.Union[int, float]

    # Total number of days/hours manually adjusted.
    totalAdminAdjustments: typing.Union[int, float]

    # Total number of days/hours adjusted.
    totalSystemAdjustments: typing.Union[int, float]

    # Annual allowance.
    annualAllowance: typing.Union[int, float]

    # Policy name.
    policy: str

class BalanceResult(RequiredBalanceResult, OptionalBalanceResult):
    pass