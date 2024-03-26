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


class AdjustmentRequest(BaseModel):
    # Adjustment type - balance or time used.
    adjustment_type: typing.Optional[Literal["balance", "daysUsed"]] = Field(None, alias='adjustmentType')

    # Policy type name.
    policy_type: typing.Optional[str] = Field(None, alias='policyType')

    # The date this adjustment becomes effective.
    effective_date: typing.Optional[date] = Field(None, alias='effectiveDate')

    # The amount of days/hours to add/subtract.
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # A reason for this adjustment.
    reason: typing.Optional[str] = Field(None, alias='reason')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
