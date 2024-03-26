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

from hi_bob_python_sdk.type.employee_termination_notice_period import EmployeeTerminationNoticePeriod

class RequiredEmployeeTermination(TypedDict):
    # The employee's termination date
    terminationDate: date

class OptionalEmployeeTermination(TypedDict, total=False):
    # The ID of the 'terminationReason' list entry
    terminationReason: str

    # The ID of the 'lifecycleReasonType' list entry
    reasonType: str

    noticePeriod: EmployeeTerminationNoticePeriod

    lastDayOfWork: date

class EmployeeTermination(RequiredEmployeeTermination, OptionalEmployeeTermination):
    pass