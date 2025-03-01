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


class ObjectsMetadata(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            id = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def fieldType() -> typing.Type['ObjectsMetadataFieldType']:
                return ObjectsMetadataFieldType
        
            @staticmethod
            def jsonPath() -> typing.Type['ObjectsMetadataJsonPath']:
                return ObjectsMetadataJsonPath
            __annotations__ = {
                "description": description,
                "id": id,
                "name": name,
                "fieldType": fieldType,
                "jsonPath": jsonPath,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldType"]) -> 'ObjectsMetadataFieldType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jsonPath"]) -> 'ObjectsMetadataJsonPath': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "fieldType", "jsonPath", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldType"]) -> typing.Union['ObjectsMetadataFieldType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jsonPath"]) -> typing.Union['ObjectsMetadataJsonPath', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "fieldType", "jsonPath", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        fieldType: typing.Union['ObjectsMetadataFieldType', schemas.Unset] = schemas.unset,
        jsonPath: typing.Union['ObjectsMetadataJsonPath', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObjectsMetadata':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            name=name,
            fieldType=fieldType,
            jsonPath=jsonPath,
            _configuration=_configuration,
            **kwargs,
        )

from hi_bob_python_sdk.model.objects_metadata_field_type import ObjectsMetadataFieldType
from hi_bob_python_sdk.model.objects_metadata_json_path import ObjectsMetadataJsonPath
