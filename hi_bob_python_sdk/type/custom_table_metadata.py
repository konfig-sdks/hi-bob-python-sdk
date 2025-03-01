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

from hi_bob_python_sdk.type.custom_table_column import CustomTableColumn

class RequiredCustomTableMetadata(TypedDict):
    pass

class OptionalCustomTableMetadata(TypedDict, total=False):
    # The description of custom table
    description: str

    # The identifier of custom table
    id: str

    # The ID of the category to which the custom table belongs
    category: str

    # The name of custom table
    name: str

    columns: typing.List[CustomTableColumn]

class CustomTableMetadata(RequiredCustomTableMetadata, OptionalCustomTableMetadata):
    pass
