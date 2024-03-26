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


class Employee(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            firstName = schemas.StrSchema
            surname = schemas.StrSchema
            email = schemas.StrSchema
            displayName = schemas.StrSchema
        
            @staticmethod
            def personal() -> typing.Type['PersonalPart']:
                return PersonalPart
        
            @staticmethod
            def about() -> typing.Type['AboutPart']:
                return AboutPart
        
            @staticmethod
            def work() -> typing.Type['WorkPart']:
                return WorkPart
            __annotations__ = {
                "id": id,
                "firstName": firstName,
                "surname": surname,
                "email": email,
                "displayName": displayName,
                "personal": personal,
                "about": about,
                "work": work,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surname"]) -> MetaOapg.properties.surname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal"]) -> 'PersonalPart': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["about"]) -> 'AboutPart': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work"]) -> 'WorkPart': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "firstName", "surname", "email", "displayName", "personal", "about", "work", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surname"]) -> typing.Union[MetaOapg.properties.surname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal"]) -> typing.Union['PersonalPart', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["about"]) -> typing.Union['AboutPart', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work"]) -> typing.Union['WorkPart', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "firstName", "surname", "email", "displayName", "personal", "about", "work", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        surname: typing.Union[MetaOapg.properties.surname, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        personal: typing.Union['PersonalPart', schemas.Unset] = schemas.unset,
        about: typing.Union['AboutPart', schemas.Unset] = schemas.unset,
        work: typing.Union['WorkPart', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Employee':
        return super().__new__(
            cls,
            *args,
            id=id,
            firstName=firstName,
            surname=surname,
            email=email,
            displayName=displayName,
            personal=personal,
            about=about,
            work=work,
            _configuration=_configuration,
            **kwargs,
        )

from hi_bob_python_sdk.model.about_part import AboutPart
from hi_bob_python_sdk.model.personal_part import PersonalPart
from hi_bob_python_sdk.model.work_part import WorkPart