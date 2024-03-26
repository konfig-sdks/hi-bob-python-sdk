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


class TimeoffRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            employeeId = schemas.UUIDSchema
            requestId = schemas.IntSchema
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
            startDatePortion = schemas.StrSchema
            endDate = schemas.DateSchema
            endDatePortion = schemas.StrSchema
            dayPortion = schemas.StrSchema
            approved = schemas.BoolSchema
            date = schemas.DateSchema
            hoursOnDate = schemas.IntSchema
            dailyHours = schemas.NumberSchema
            
            
            class durationUnit(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DAYS(cls):
                    return cls("days")
                
                @schemas.classproperty
                def HOURS(cls):
                    return cls("hours")
            totalDuration = schemas.NumberSchema
            totalCost = schemas.NumberSchema
            status = schemas.StrSchema
            hasAttachment = schemas.BoolSchema
            reasonCode = schemas.StrSchema
        
            @staticmethod
            def attachmentLinks() -> typing.Type['TimeoffRequestAttachmentLinks']:
                return TimeoffRequestAttachmentLinks
            __annotations__ = {
                "description": description,
                "employeeId": employeeId,
                "requestId": requestId,
                "policyTypeDisplayName": policyTypeDisplayName,
                "type": type,
                "startDate": startDate,
                "startDatePortion": startDatePortion,
                "endDate": endDate,
                "endDatePortion": endDatePortion,
                "dayPortion": dayPortion,
                "approved": approved,
                "date": date,
                "hoursOnDate": hoursOnDate,
                "dailyHours": dailyHours,
                "durationUnit": durationUnit,
                "totalDuration": totalDuration,
                "totalCost": totalCost,
                "status": status,
                "hasAttachment": hasAttachment,
                "reasonCode": reasonCode,
                "attachmentLinks": attachmentLinks,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestId"]) -> MetaOapg.properties.requestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policyTypeDisplayName"]) -> MetaOapg.properties.policyTypeDisplayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDatePortion"]) -> MetaOapg.properties.startDatePortion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDatePortion"]) -> MetaOapg.properties.endDatePortion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayPortion"]) -> MetaOapg.properties.dayPortion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approved"]) -> MetaOapg.properties.approved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hoursOnDate"]) -> MetaOapg.properties.hoursOnDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dailyHours"]) -> MetaOapg.properties.dailyHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["durationUnit"]) -> MetaOapg.properties.durationUnit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalDuration"]) -> MetaOapg.properties.totalDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCost"]) -> MetaOapg.properties.totalCost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasAttachment"]) -> MetaOapg.properties.hasAttachment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reasonCode"]) -> MetaOapg.properties.reasonCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachmentLinks"]) -> 'TimeoffRequestAttachmentLinks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "employeeId", "requestId", "policyTypeDisplayName", "type", "startDate", "startDatePortion", "endDate", "endDatePortion", "dayPortion", "approved", "date", "hoursOnDate", "dailyHours", "durationUnit", "totalDuration", "totalCost", "status", "hasAttachment", "reasonCode", "attachmentLinks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestId"]) -> typing.Union[MetaOapg.properties.requestId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policyTypeDisplayName"]) -> typing.Union[MetaOapg.properties.policyTypeDisplayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDatePortion"]) -> typing.Union[MetaOapg.properties.startDatePortion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDatePortion"]) -> typing.Union[MetaOapg.properties.endDatePortion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayPortion"]) -> typing.Union[MetaOapg.properties.dayPortion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approved"]) -> typing.Union[MetaOapg.properties.approved, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hoursOnDate"]) -> typing.Union[MetaOapg.properties.hoursOnDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dailyHours"]) -> typing.Union[MetaOapg.properties.dailyHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["durationUnit"]) -> typing.Union[MetaOapg.properties.durationUnit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalDuration"]) -> typing.Union[MetaOapg.properties.totalDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCost"]) -> typing.Union[MetaOapg.properties.totalCost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasAttachment"]) -> typing.Union[MetaOapg.properties.hasAttachment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reasonCode"]) -> typing.Union[MetaOapg.properties.reasonCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachmentLinks"]) -> typing.Union['TimeoffRequestAttachmentLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "employeeId", "requestId", "policyTypeDisplayName", "type", "startDate", "startDatePortion", "endDate", "endDatePortion", "dayPortion", "approved", "date", "hoursOnDate", "dailyHours", "durationUnit", "totalDuration", "totalCost", "status", "hasAttachment", "reasonCode", "attachmentLinks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        requestId: typing.Union[MetaOapg.properties.requestId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        policyTypeDisplayName: typing.Union[MetaOapg.properties.policyTypeDisplayName, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, schemas.Unset] = schemas.unset,
        startDatePortion: typing.Union[MetaOapg.properties.startDatePortion, str, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, schemas.Unset] = schemas.unset,
        endDatePortion: typing.Union[MetaOapg.properties.endDatePortion, str, schemas.Unset] = schemas.unset,
        dayPortion: typing.Union[MetaOapg.properties.dayPortion, str, schemas.Unset] = schemas.unset,
        approved: typing.Union[MetaOapg.properties.approved, bool, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, date, schemas.Unset] = schemas.unset,
        hoursOnDate: typing.Union[MetaOapg.properties.hoursOnDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dailyHours: typing.Union[MetaOapg.properties.dailyHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        durationUnit: typing.Union[MetaOapg.properties.durationUnit, str, schemas.Unset] = schemas.unset,
        totalDuration: typing.Union[MetaOapg.properties.totalDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalCost: typing.Union[MetaOapg.properties.totalCost, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        hasAttachment: typing.Union[MetaOapg.properties.hasAttachment, bool, schemas.Unset] = schemas.unset,
        reasonCode: typing.Union[MetaOapg.properties.reasonCode, str, schemas.Unset] = schemas.unset,
        attachmentLinks: typing.Union['TimeoffRequestAttachmentLinks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeoffRequest':
        return super().__new__(
            cls,
            *args,
            description=description,
            employeeId=employeeId,
            requestId=requestId,
            policyTypeDisplayName=policyTypeDisplayName,
            type=type,
            startDate=startDate,
            startDatePortion=startDatePortion,
            endDate=endDate,
            endDatePortion=endDatePortion,
            dayPortion=dayPortion,
            approved=approved,
            date=date,
            hoursOnDate=hoursOnDate,
            dailyHours=dailyHours,
            durationUnit=durationUnit,
            totalDuration=totalDuration,
            totalCost=totalCost,
            status=status,
            hasAttachment=hasAttachment,
            reasonCode=reasonCode,
            attachmentLinks=attachmentLinks,
            _configuration=_configuration,
            **kwargs,
        )

from hi_bob_python_sdk.model.timeoff_request_attachment_links import TimeoffRequestAttachmentLinks