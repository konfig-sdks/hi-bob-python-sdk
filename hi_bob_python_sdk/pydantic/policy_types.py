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

from hi_bob_python_sdk.pydantic.policy_types_policy_types import PolicyTypesPolicyTypes

class PolicyTypes(BaseModel):
    policy_types: typing.Optional[PolicyTypesPolicyTypes] = Field(None, alias='policyTypes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
