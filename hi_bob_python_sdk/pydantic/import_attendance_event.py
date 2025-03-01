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


class ImportAttendanceEvent(BaseModel):
    # The id value to identify the customer by. Will fetch the employee based on the field (type) selected in <i>idType</i>.
    id: str = Field(alias='id')

    # The timestamp to log as a clock-in date-time in local time
    clock_in: typing.Optional[str] = Field(None, alias='clockIn')

    # The timestamp to log as a clock-out date-time in local time.
    clock_out: typing.Optional[str] = Field(None, alias='clockOut')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
