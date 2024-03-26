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


class RequiredSubmitTimeoffRequest(TypedDict):
    # Request policy type, e.g. Holiday, Sick or any custom type defined.
    policyType: str

    # Date of the first day of the time off (not relevant for requests using the hours type).
    startDate: date

class OptionalSubmitTimeoffRequest(TypedDict, total=False):
    # Request reason.
    description: str

    # The type of request duration.<br> Select <b>hours</b> when the request is for X hours during the day requested (This is supported only for policy types measured in hours).<br> Select <b>portionOnRange</b> when the  request is for every morning or every afternoon during the days requested.<br> Select <b>hoursOnRange</b> when the request is for X hours every day during the days requested (This is supported only for policy types measured in hours)
    requestRangeType: str

    # Portion of the first day - relevant for requests in days.
    startDatePortion: str

    # Date of the last day of the time off (not relevant for requests using                                                the hours type).
    endDate: date

    # This field is mandatory if the requestRangeType is set to 'hours'.
    hours: int

    # Relevant if requestRangeType is set to 'hours'.
    minutes: int

    # Portion of the last day - relevant for requests in days.
    endDatePortion: str

    # Select <b>morning</b> when the request is for mornings on the days requested. Select <b>afternoon</b> when the request is for afternoons on the days requested.<br> This is mandatory if the <b>requestRangeType</b> is <b>portionOnRange</b>.
    dayPortion: str

    # Enter the number of hours when the request is for X hours on the days requested.<br> This is mandatory if the <b>requestRangeType</b> is <b>hoursOnRange</b>.
    dailyHours: int

    # Enter the number of minutes when the request is for X hours and X minutes on the days requested.<br> This is relevant if the <b>requestRangeType</b> is <b>hoursOnRange</b> and the amount requested is not a full hour or hours.
    dailyMinutes: int

    # Admins only can skip the approval policy. Setting this field to true will create an approved request.
    skipManagerApproval: bool

    # The employee ID of the user to be set as the approver for this request. This is relevant if 'skipManagerApproval' is set to true.<br>Please note that the user calling the API with this param must have permission to import time off requests.
    approver: str

    # The reason code ID taken from the policy type's reason codes list. The list is available in GET /timeoff/policy-types/{policyType}/reason-codes
    reasonCode: int

class SubmitTimeoffRequest(RequiredSubmitTimeoffRequest, OptionalSubmitTimeoffRequest):
    pass
