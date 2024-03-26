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

from hi_bob_python_sdk.pydantic.import_attendance_event import ImportAttendanceEvent

class ImportAttendanceData(BaseModel):
    # The ID type used to identify the employee. Can be one of: \"bobId\", \"email\", \"idInCompany\", or a custom field.<br/>For <b>custom fields</b> a forward slash separator should be used.<br/>In order to use a specific custom field to identify an employee, for example a custom field called \"Payroll integration ID\":<ul><li>Query the field name via the <a href='https://apidocs.hibob.com/reference/get_company-people-fields'>\"Get all company fields\"</a></li><li>In the response the name will look like <b>\"identification.custom.Payroll Integration ID_1RNhIIf\"</b></li><li>The value to use should be: <b>\"/identification/custom/Payroll Integration ID_1RNhI\"</b></li></ul>
    id_type: str = Field(alias='idType')

    # List of attendance events
    requests: typing.List[ImportAttendanceEvent] = Field(alias='requests')

    # Allows to set custom date format for the date-time values sent in the requests
    date_time_format: typing.Optional[str] = Field(None, alias='dateTimeFormat')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )