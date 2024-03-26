# coding: utf-8

"""
    Bob API

    Access your employees data with the Bob API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from hi_bob_python_sdk import schemas  # noqa: F401


class PeopleUpdateEmployeeRecordRequestAbout(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def hobbies() -> typing.Type['PeopleUpdateEmployeeRecordRequestAboutHobbies']:
                return PeopleUpdateEmployeeRecordRequestAboutHobbies
            __annotations__ = {
                "hobbies": hobbies,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hobbies"]) -> 'PeopleUpdateEmployeeRecordRequestAboutHobbies': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hobbies", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hobbies"]) -> typing.Union['PeopleUpdateEmployeeRecordRequestAboutHobbies', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hobbies", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hobbies: typing.Union['PeopleUpdateEmployeeRecordRequestAboutHobbies', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PeopleUpdateEmployeeRecordRequestAbout':
        return super().__new__(
            cls,
            *args,
            hobbies=hobbies,
            _configuration=_configuration,
            **kwargs,
        )

from hi_bob_python_sdk.model.people_update_employee_record_request_about_hobbies import PeopleUpdateEmployeeRecordRequestAboutHobbies
