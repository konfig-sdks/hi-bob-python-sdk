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


class OutToday(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            employeeId = schemas.UUIDSchema
            employeeDisplayName = schemas.StrSchema
            employeeEmail = schemas.StrSchema
            policyTypeDisplayName = schemas.StrSchema
            startDate = schemas.DateSchema
            startDatePortion = schemas.StrSchema
            endDate = schemas.DateSchema
            endDatePortion = schemas.StrSchema
            
            
            class requestRangeType(
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
            dayPortion = schemas.StrSchema
            dailyHours = schemas.NumberSchema
            date = schemas.DateSchema
            hours = schemas.IntSchema
            minutes = schemas.IntSchema
            __annotations__ = {
                "employeeId": employeeId,
                "employeeDisplayName": employeeDisplayName,
                "employeeEmail": employeeEmail,
                "policyTypeDisplayName": policyTypeDisplayName,
                "startDate": startDate,
                "startDatePortion": startDatePortion,
                "endDate": endDate,
                "endDatePortion": endDatePortion,
                "requestRangeType": requestRangeType,
                "dayPortion": dayPortion,
                "dailyHours": dailyHours,
                "date": date,
                "hours": hours,
                "minutes": minutes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeDisplayName"]) -> MetaOapg.properties.employeeDisplayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeEmail"]) -> MetaOapg.properties.employeeEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policyTypeDisplayName"]) -> MetaOapg.properties.policyTypeDisplayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDatePortion"]) -> MetaOapg.properties.startDatePortion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDatePortion"]) -> MetaOapg.properties.endDatePortion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestRangeType"]) -> MetaOapg.properties.requestRangeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayPortion"]) -> MetaOapg.properties.dayPortion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dailyHours"]) -> MetaOapg.properties.dailyHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours"]) -> MetaOapg.properties.hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minutes"]) -> MetaOapg.properties.minutes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "employeeDisplayName", "employeeEmail", "policyTypeDisplayName", "startDate", "startDatePortion", "endDate", "endDatePortion", "requestRangeType", "dayPortion", "dailyHours", "date", "hours", "minutes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeDisplayName"]) -> typing.Union[MetaOapg.properties.employeeDisplayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeEmail"]) -> typing.Union[MetaOapg.properties.employeeEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policyTypeDisplayName"]) -> typing.Union[MetaOapg.properties.policyTypeDisplayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDatePortion"]) -> typing.Union[MetaOapg.properties.startDatePortion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDatePortion"]) -> typing.Union[MetaOapg.properties.endDatePortion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestRangeType"]) -> typing.Union[MetaOapg.properties.requestRangeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayPortion"]) -> typing.Union[MetaOapg.properties.dayPortion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dailyHours"]) -> typing.Union[MetaOapg.properties.dailyHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours"]) -> typing.Union[MetaOapg.properties.hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minutes"]) -> typing.Union[MetaOapg.properties.minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "employeeDisplayName", "employeeEmail", "policyTypeDisplayName", "startDate", "startDatePortion", "endDate", "endDatePortion", "requestRangeType", "dayPortion", "dailyHours", "date", "hours", "minutes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        employeeDisplayName: typing.Union[MetaOapg.properties.employeeDisplayName, str, schemas.Unset] = schemas.unset,
        employeeEmail: typing.Union[MetaOapg.properties.employeeEmail, str, schemas.Unset] = schemas.unset,
        policyTypeDisplayName: typing.Union[MetaOapg.properties.policyTypeDisplayName, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, schemas.Unset] = schemas.unset,
        startDatePortion: typing.Union[MetaOapg.properties.startDatePortion, str, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, schemas.Unset] = schemas.unset,
        endDatePortion: typing.Union[MetaOapg.properties.endDatePortion, str, schemas.Unset] = schemas.unset,
        requestRangeType: typing.Union[MetaOapg.properties.requestRangeType, str, schemas.Unset] = schemas.unset,
        dayPortion: typing.Union[MetaOapg.properties.dayPortion, str, schemas.Unset] = schemas.unset,
        dailyHours: typing.Union[MetaOapg.properties.dailyHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, date, schemas.Unset] = schemas.unset,
        hours: typing.Union[MetaOapg.properties.hours, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minutes: typing.Union[MetaOapg.properties.minutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OutToday':
        return super().__new__(
            cls,
            *args,
            employeeId=employeeId,
            employeeDisplayName=employeeDisplayName,
            employeeEmail=employeeEmail,
            policyTypeDisplayName=policyTypeDisplayName,
            startDate=startDate,
            startDatePortion=startDatePortion,
            endDate=endDate,
            endDatePortion=endDatePortion,
            requestRangeType=requestRangeType,
            dayPortion=dayPortion,
            dailyHours=dailyHours,
            date=date,
            hours=hours,
            minutes=minutes,
            _configuration=_configuration,
            **kwargs,
        )
