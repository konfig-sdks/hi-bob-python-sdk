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


class Request(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            requestId = schemas.Int64Schema
            employeeId = schemas.UUIDSchema
            policyType = schemas.StrSchema
            policyTypeDisplayName = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DAYS(cls):
                    return cls("days")
                
                @schemas.classproperty
                def HOURS(cls):
                    return cls("hours")
                
                @schemas.classproperty
                def PORTION_ON_RANGE(cls):
                    return cls("portionOnRange")
                
                @schemas.classproperty
                def HOURS_ON_RANGE(cls):
                    return cls("hoursOnRange")
            startDate = schemas.DateSchema
            startPortion = schemas.StrSchema
            endDate = schemas.DateSchema
            endPortion = schemas.StrSchema
            dayPortion = schemas.StrSchema
            date = schemas.DateSchema
            hoursOnDate = schemas.IntSchema
            minutes = schemas.IntSchema
            dailyHours = schemas.NumberSchema
            status = schemas.StrSchema
            employeeDisplayName = schemas.StrSchema
            __annotations__ = {
                "requestId": requestId,
                "employeeId": employeeId,
                "policyType": policyType,
                "policyTypeDisplayName": policyTypeDisplayName,
                "type": type,
                "startDate": startDate,
                "startPortion": startPortion,
                "endDate": endDate,
                "endPortion": endPortion,
                "dayPortion": dayPortion,
                "date": date,
                "hoursOnDate": hoursOnDate,
                "minutes": minutes,
                "dailyHours": dailyHours,
                "status": status,
                "employeeDisplayName": employeeDisplayName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestId"]) -> MetaOapg.properties.requestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policyType"]) -> MetaOapg.properties.policyType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policyTypeDisplayName"]) -> MetaOapg.properties.policyTypeDisplayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startPortion"]) -> MetaOapg.properties.startPortion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endPortion"]) -> MetaOapg.properties.endPortion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayPortion"]) -> MetaOapg.properties.dayPortion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hoursOnDate"]) -> MetaOapg.properties.hoursOnDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minutes"]) -> MetaOapg.properties.minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dailyHours"]) -> MetaOapg.properties.dailyHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeDisplayName"]) -> MetaOapg.properties.employeeDisplayName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["requestId", "employeeId", "policyType", "policyTypeDisplayName", "type", "startDate", "startPortion", "endDate", "endPortion", "dayPortion", "date", "hoursOnDate", "minutes", "dailyHours", "status", "employeeDisplayName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestId"]) -> typing.Union[MetaOapg.properties.requestId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policyType"]) -> typing.Union[MetaOapg.properties.policyType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policyTypeDisplayName"]) -> typing.Union[MetaOapg.properties.policyTypeDisplayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startPortion"]) -> typing.Union[MetaOapg.properties.startPortion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endPortion"]) -> typing.Union[MetaOapg.properties.endPortion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayPortion"]) -> typing.Union[MetaOapg.properties.dayPortion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hoursOnDate"]) -> typing.Union[MetaOapg.properties.hoursOnDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minutes"]) -> typing.Union[MetaOapg.properties.minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dailyHours"]) -> typing.Union[MetaOapg.properties.dailyHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeDisplayName"]) -> typing.Union[MetaOapg.properties.employeeDisplayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["requestId", "employeeId", "policyType", "policyTypeDisplayName", "type", "startDate", "startPortion", "endDate", "endPortion", "dayPortion", "date", "hoursOnDate", "minutes", "dailyHours", "status", "employeeDisplayName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        requestId: typing.Union[MetaOapg.properties.requestId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        policyType: typing.Union[MetaOapg.properties.policyType, str, schemas.Unset] = schemas.unset,
        policyTypeDisplayName: typing.Union[MetaOapg.properties.policyTypeDisplayName, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, schemas.Unset] = schemas.unset,
        startPortion: typing.Union[MetaOapg.properties.startPortion, str, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, schemas.Unset] = schemas.unset,
        endPortion: typing.Union[MetaOapg.properties.endPortion, str, schemas.Unset] = schemas.unset,
        dayPortion: typing.Union[MetaOapg.properties.dayPortion, str, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, date, schemas.Unset] = schemas.unset,
        hoursOnDate: typing.Union[MetaOapg.properties.hoursOnDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minutes: typing.Union[MetaOapg.properties.minutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dailyHours: typing.Union[MetaOapg.properties.dailyHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        employeeDisplayName: typing.Union[MetaOapg.properties.employeeDisplayName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Request':
        return super().__new__(
            cls,
            *args,
            requestId=requestId,
            employeeId=employeeId,
            policyType=policyType,
            policyTypeDisplayName=policyTypeDisplayName,
            type=type,
            startDate=startDate,
            startPortion=startPortion,
            endDate=endDate,
            endPortion=endPortion,
            dayPortion=dayPortion,
            date=date,
            hoursOnDate=hoursOnDate,
            minutes=minutes,
            dailyHours=dailyHours,
            status=status,
            employeeDisplayName=employeeDisplayName,
            _configuration=_configuration,
            **kwargs,
        )
