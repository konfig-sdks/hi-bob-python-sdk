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


class ImportAttendanceResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "success": "SUCCESS",
                        "failed": "FAILED",
                        "partial_success": "PARTIAL_SUCCESS",
                    }
                
                @schemas.classproperty
                def SUCCESS(cls):
                    return cls("success")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("failed")
                
                @schemas.classproperty
                def PARTIAL_SUCCESS(cls):
                    return cls("partial_success")
            total = schemas.NumberSchema
            imported = schemas.NumberSchema
            notImported = schemas.NumberSchema
        
            @staticmethod
            def errors() -> typing.Type['ImportAttendanceResponseErrors']:
                return ImportAttendanceResponseErrors
            __annotations__ = {
                "status": status,
                "total": total,
                "imported": imported,
                "notImported": notImported,
                "errors": errors,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imported"]) -> MetaOapg.properties.imported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notImported"]) -> MetaOapg.properties.notImported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'ImportAttendanceResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "total", "imported", "notImported", "errors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imported"]) -> typing.Union[MetaOapg.properties.imported, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notImported"]) -> typing.Union[MetaOapg.properties.notImported, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union['ImportAttendanceResponseErrors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "total", "imported", "notImported", "errors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        imported: typing.Union[MetaOapg.properties.imported, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        notImported: typing.Union[MetaOapg.properties.notImported, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        errors: typing.Union['ImportAttendanceResponseErrors', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImportAttendanceResponse':
        return super().__new__(
            cls,
            *args,
            status=status,
            total=total,
            imported=imported,
            notImported=notImported,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )

from hi_bob_python_sdk.model.import_attendance_response_errors import ImportAttendanceResponseErrors
