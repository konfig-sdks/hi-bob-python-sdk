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


class CreateFieldRequest(BaseModel):
    # The name of the field.
    name: str = Field(alias='name')

    # The category of the field.
    category: str = Field(alias='category')

    # The type of field. Supported field types: text, text-area, number, date, list, multi-list, hierarchy-list, currency, employee-reference, document.
    type: str = Field(alias='type')

    # The description of the field.
    description: typing.Optional[str] = Field(None, alias='description')

    # When true, this field keeps the history of its values, each being active starting from a certain date. The default value is false.
    historical: typing.Optional[str] = Field(None, alias='historical')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
