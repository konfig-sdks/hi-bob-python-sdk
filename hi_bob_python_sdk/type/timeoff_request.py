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

from hi_bob_python_sdk.type.timeoff_request_attachment_links import TimeoffRequestAttachmentLinks

class RequiredTimeoffRequest(TypedDict):
    pass

class OptionalTimeoffRequest(TypedDict, total=False):
    # The request description.
    description: str

    # Employee ID.
    employeeId: str

    # Time Off Request ID.
    requestId: int

    # Display name of the policy type.
    policyTypeDisplayName: str

    # The type of request duration.<br> <b>portionOnRange</b> is when the request is for every morning or every afternoon during the days requested.<br> <b>hoursOnRange</b> is when the request is for X hours every day during the days requested.
    type: str

    # Date of the first day of the time off  (not relevant for requests using the hours type).
    startDate: date

    # What portion of the first day is included - all_day, morning or afternoon (relevant for requests using the Days type).
    startDatePortion: str

    # Date of the last day of the time off (not relevant for requests using                                                the hours type).
    endDate: date

    # What portion of the last day is included - all_day, morning or afternoon (relevant for requests using the Days type).
    endDatePortion: str

    # What portion of the request's days is included - morning or afternoon (relevant for requests using the portionOnRange type).
    dayPortion: str

    # Whether the request is approved (and hence publicly visible).
    approved: bool

    # Date of the time off (relevant for requests using the Hours type).
    date: date

    # The time off duration in hours for the date (relevant for requests using the Hours type)
    hoursOnDate: int

    # The time off duration in hours for every day in the request (relevant for requests using the hoursOnRange type).
    dailyHours: typing.Union[int, float]

    # The unit used for the totalDuration and totalCost - either 'days' or 'hours'
    durationUnit: str

    # The total amount of time the request covers, including regular days off such as weekends
    totalDuration: typing.Union[int, float]

    # The amount that will be deducted from the balance
    totalCost: typing.Union[int, float]

    # Request status. This can be approved, pending, canceled, etc.
    status: str

    # Whether the request has attachments
    hasAttachment: bool

    # The reason code taken from the policy type's reason codes list. The list is available in GET /timeoff/policy-types/{policyType}/reason-codes
    reasonCode: str

    attachmentLinks: TimeoffRequestAttachmentLinks

class TimeoffRequest(RequiredTimeoffRequest, OptionalTimeoffRequest):
    pass
