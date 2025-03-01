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


class EmployeeDocumentResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class documents(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmployeeDocumentWithDownloadLink']:
                        return EmployeeDocumentWithDownloadLink
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EmployeeDocumentWithDownloadLink'], typing.List['EmployeeDocumentWithDownloadLink']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'documents':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EmployeeDocumentWithDownloadLink':
                    return super().__getitem__(i)
            __annotations__ = {
                "documents": documents,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documents"]) -> MetaOapg.properties.documents: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["documents", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documents"]) -> typing.Union[MetaOapg.properties.documents, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["documents", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        documents: typing.Union[MetaOapg.properties.documents, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeDocumentResponse':
        return super().__new__(
            cls,
            *args,
            documents=documents,
            _configuration=_configuration,
            **kwargs,
        )

from hi_bob_python_sdk.model.employee_document_with_download_link import EmployeeDocumentWithDownloadLink
