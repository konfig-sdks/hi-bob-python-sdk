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

from hi_bob_python_sdk.pydantic.people_update_employee_record_request_about_hobbies import PeopleUpdateEmployeeRecordRequestAboutHobbies

class PeopleUpdateEmployeeRecordRequestAbout(BaseModel):
    hobbies: typing.Optional[PeopleUpdateEmployeeRecordRequestAboutHobbies] = Field(None, alias='hobbies')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
