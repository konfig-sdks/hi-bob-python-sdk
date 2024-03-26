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


class RequiredSubmitTimeoffRequestDiffHoursDurationsItem(TypedDict):
    # Date of the duration.
    date: date

    # The number of hours in the duration.
    hours: int

    # The number of minutes in the duration.
    minutes: int

class OptionalSubmitTimeoffRequestDiffHoursDurationsItem(TypedDict, total=False):
    pass

class SubmitTimeoffRequestDiffHoursDurationsItem(RequiredSubmitTimeoffRequestDiffHoursDurationsItem, OptionalSubmitTimeoffRequestDiffHoursDurationsItem):
    pass