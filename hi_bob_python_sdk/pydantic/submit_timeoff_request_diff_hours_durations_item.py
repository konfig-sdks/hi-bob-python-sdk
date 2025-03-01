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


class SubmitTimeoffRequestDiffHoursDurationsItem(BaseModel):
    # Date of the duration.
    date: date = Field(alias='date')

    # The number of hours in the duration.
    hours: int = Field(alias='hours')

    # The number of minutes in the duration.
    minutes: int = Field(alias='minutes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
