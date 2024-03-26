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

from hi_bob_python_sdk.type.import_attendance_response_errors import ImportAttendanceResponseErrors

class RequiredImportAttendanceResponse(TypedDict):
    pass

class OptionalImportAttendanceResponse(TypedDict, total=False):
    # Import status
    status: str

    # Total number of clock-in and clock-out events received
    total: typing.Union[int, float]

    # Number of clock-in/clock-out events imported
    imported: typing.Union[int, float]

    # Number of clock-in/clock-out events which were not imported
    notImported: typing.Union[int, float]

    errors: ImportAttendanceResponseErrors

class ImportAttendanceResponse(RequiredImportAttendanceResponse, OptionalImportAttendanceResponse):
    pass