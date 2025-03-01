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


class EmployeeDocumentWithDownloadLink(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            documentName = schemas.StrSchema
            downloadLink = schemas.StrSchema
            __annotations__ = {
                "documentName": documentName,
                "downloadLink": downloadLink,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentName"]) -> MetaOapg.properties.documentName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["downloadLink"]) -> MetaOapg.properties.downloadLink: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["documentName", "downloadLink", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentName"]) -> typing.Union[MetaOapg.properties.documentName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["downloadLink"]) -> typing.Union[MetaOapg.properties.downloadLink, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["documentName", "downloadLink", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        documentName: typing.Union[MetaOapg.properties.documentName, str, schemas.Unset] = schemas.unset,
        downloadLink: typing.Union[MetaOapg.properties.downloadLink, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeDocumentWithDownloadLink':
        return super().__new__(
            cls,
            *args,
            documentName=documentName,
            downloadLink=downloadLink,
            _configuration=_configuration,
            **kwargs,
        )
