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

from hi_bob_python_sdk.pydantic.objects_metadata_field_type import ObjectsMetadataFieldType
from hi_bob_python_sdk.pydantic.objects_metadata_json_path import ObjectsMetadataJsonPath

class ObjectsMetadata(BaseModel):
    # Description of the field.
    description: typing.Optional[str] = Field(None, alias='description')

    # ID of the field.
    id: typing.Optional[str] = Field(None, alias='id')

    # Name of the field.
    name: typing.Optional[str] = Field(None, alias='name')

    field_type: typing.Optional[ObjectsMetadataFieldType] = Field(None, alias='fieldType')

    json_path: typing.Optional[ObjectsMetadataJsonPath] = Field(None, alias='jsonPath')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
