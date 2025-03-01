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


class OutToday(BaseModel):
    # Employee ID.
    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    # Employee display name.
    employee_display_name: typing.Optional[str] = Field(None, alias='employeeDisplayName')

    # Employee email address.
    employee_email: typing.Optional[str] = Field(None, alias='employeeEmail')

    # Display name of the policy type.
    policy_type_display_name: typing.Optional[str] = Field(None, alias='policyTypeDisplayName')

    # Date of the first day of the time off (not relevant for requests using the hours type).
    start_date: typing.Optional[date] = Field(None, alias='startDate')

    # What portion of the first day is included - all_day, morning or afternoon (relevant for request using the days type).
    start_date_portion: typing.Optional[str] = Field(None, alias='startDatePortion')

    # Date of the last day of the time off (not relevant for requests using the hours type).
    end_date: typing.Optional[date] = Field(None, alias='endDate')

    # What portion of the last day is included - all_day, morning or afternoon (relevant for request using the days type).
    end_date_portion: typing.Optional[str] = Field(None, alias='endDatePortion')

    # The type of request duration.<br> <b>portionOnRange</b> is when the request is for every morning or every afternoon during the days requested.<br> <b>hoursOnRange</b> is when the request is for X hours every day during the days requested.
    request_range_type: typing.Optional[Literal["days", "hours", "portionOnRange", "hoursOnRange"]] = Field(None, alias='requestRangeType')

    # What portion of the request's days is included - morning or afternoon (relevant for request using the portionOnRange type).
    day_portion: typing.Optional[str] = Field(None, alias='dayPortion')

    # The time off duration in hours for every request's days (relevant for requests with hoursOnRange type).
    daily_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='dailyHours')

    # Date of the time off (relevant for requests using the hours type).
    date: typing.Optional[date] = Field(None, alias='date')

    # The time off duration in hours for the date (relevant for requests with hours type).
    hours: typing.Optional[int] = Field(None, alias='hours')

    # Relevant for requests using the hours type.
    minutes: typing.Optional[int] = Field(None, alias='minutes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
