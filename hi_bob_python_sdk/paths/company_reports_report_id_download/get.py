# coding: utf-8

"""
    Bob API

    Access your employees data with the Bob API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from hi_bob_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from hi_bob_python_sdk.api_response import AsyncGeneratorResponse
from hi_bob_python_sdk import api_client, exceptions
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

from hi_bob_python_sdk.model.error import Error as ErrorSchema

from hi_bob_python_sdk.type.error import Error

from ...api_client import Dictionary
from hi_bob_python_sdk.pydantic.error import Error as ErrorPydantic

from . import path

# Query params


class FormatSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "csv": "CSV",
            "xlsx": "XLSX",
            "json": "JSON",
        }
    
    @schemas.classproperty
    def CSV(cls):
        return cls("csv")
    
    @schemas.classproperty
    def XLSX(cls):
        return cls("xlsx")
    
    @schemas.classproperty
    def JSON(cls):
        return cls("json")
IncludeInfoSchema = schemas.BoolSchema
LocaleSchema = schemas.StrSchema
HumanReadableSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'format': typing.Union[FormatSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'includeInfo': typing.Union[IncludeInfoSchema, bool, ],
        'locale': typing.Union[LocaleSchema, str, ],
        'humanReadable': typing.Union[HumanReadableSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    required=True,
    explode=True,
)
request_query_include_info = api_client.QueryParameter(
    name="includeInfo",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeInfoSchema,
    explode=True,
)
request_query_locale = api_client.QueryParameter(
    name="locale",
    style=api_client.ParameterStyle.FORM,
    schema=LocaleSchema,
    explode=True,
)
request_query_human_readable = api_client.QueryParameter(
    name="humanReadable",
    style=api_client.ParameterStyle.FORM,
    schema=HumanReadableSchema,
    explode=True,
)
# Path params
ReportIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'reportId': typing.Union[ReportIdSchema, decimal.Decimal, int, float, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_report_id = api_client.PathParameter(
    name="reportId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ReportIdSchema,
    required=True,
)
_auth = [
    'Basic',
]
SchemaFor200ResponseBodyApplicationJson = schemas.BinarySchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.IO


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.IO


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Error


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _download_by_id_mapped_args(
        self,
        report_id: typing.Union[int, float],
        format: str,
        include_info: typing.Optional[bool] = None,
        locale: typing.Optional[str] = None,
        human_readable: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if format is not None:
            _query_params["format"] = format
        if include_info is not None:
            _query_params["includeInfo"] = include_info
        if locale is not None:
            _query_params["locale"] = locale
        if human_readable is not None:
            _query_params["humanReadable"] = human_readable
        if report_id is not None:
            _path_params["reportId"] = report_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _adownload_by_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Download the report by ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_report_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
            request_query_include_info,
            request_query_locale,
            request_query_human_readable,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/reports/{reportId}/download',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _download_by_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Download the report by ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_report_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
            request_query_include_info,
            request_query_locale,
            request_query_human_readable,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/company/reports/{reportId}/download',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class DownloadByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def adownload_by_id(
        self,
        report_id: typing.Union[int, float],
        format: str,
        include_info: typing.Optional[bool] = None,
        locale: typing.Optional[str] = None,
        human_readable: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._download_by_id_mapped_args(
            report_id=report_id,
            format=format,
            include_info=include_info,
            locale=locale,
            human_readable=human_readable,
        )
        return await self._adownload_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def download_by_id(
        self,
        report_id: typing.Union[int, float],
        format: str,
        include_info: typing.Optional[bool] = None,
        locale: typing.Optional[str] = None,
        human_readable: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._download_by_id_mapped_args(
            report_id=report_id,
            format=format,
            include_info=include_info,
            locale=locale,
            human_readable=human_readable,
        )
        return self._download_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class DownloadById(BaseApi):

    async def adownload_by_id(
        self,
        report_id: typing.Union[int, float],
        format: str,
        include_info: typing.Optional[bool] = None,
        locale: typing.Optional[str] = None,
        human_readable: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> typing.IO:
        raw_response = await self.raw.adownload_by_id(
            report_id=report_id,
            format=format,
            include_info=include_info,
            locale=locale,
            human_readable=human_readable,
            **kwargs,
        )
        if validate:
            return RootModel[typing.IO](raw_response.body).root
        return raw_response.body
    
    
    def download_by_id(
        self,
        report_id: typing.Union[int, float],
        format: str,
        include_info: typing.Optional[bool] = None,
        locale: typing.Optional[str] = None,
        human_readable: typing.Optional[str] = None,
        validate: bool = False,
    ) -> typing.IO:
        raw_response = self.raw.download_by_id(
            report_id=report_id,
            format=format,
            include_info=include_info,
            locale=locale,
            human_readable=human_readable,
        )
        if validate:
            return RootModel[typing.IO](raw_response.body).root
        return raw_response.body


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        report_id: typing.Union[int, float],
        format: str,
        include_info: typing.Optional[bool] = None,
        locale: typing.Optional[str] = None,
        human_readable: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._download_by_id_mapped_args(
            report_id=report_id,
            format=format,
            include_info=include_info,
            locale=locale,
            human_readable=human_readable,
        )
        return await self._adownload_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        report_id: typing.Union[int, float],
        format: str,
        include_info: typing.Optional[bool] = None,
        locale: typing.Optional[str] = None,
        human_readable: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._download_by_id_mapped_args(
            report_id=report_id,
            format=format,
            include_info=include_info,
            locale=locale,
            human_readable=human_readable,
        )
        return self._download_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )
