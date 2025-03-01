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


class RequiredUpdateListItemRequest(TypedDict):
    pass

class OptionalUpdateListItemRequest(TypedDict, total=False):
    # Name of the item.
    name: str

    # ID of the new hierarchy parent node.
    parentId: int

class UpdateListItemRequest(RequiredUpdateListItemRequest, OptionalUpdateListItemRequest):
    pass
