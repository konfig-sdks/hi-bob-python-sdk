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
from hi_bob_python_sdk.model.requests import Requests as RequestsSchema

from hi_bob_python_sdk.type.error import Error
from hi_bob_python_sdk.type.requests import Requests

from ...api_client import Dictionary
from hi_bob_python_sdk.pydantic.error import Error as ErrorPydantic
from hi_bob_python_sdk.pydantic.requests import Requests as RequestsPydantic

# Query params
ModelFromSchema = schemas.DateSchema
ToSchema = schemas.DateSchema
IncludeHourlySchema = schemas.BoolSchema
IncludePrivateSchema = schemas.BoolSchema
IncludePendingSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'from': typing.Union[ModelFromSchema, str, date, ],
        'to': typing.Union[ToSchema, str, date, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'includeHourly': typing.Union[IncludeHourlySchema, bool, ],
        'includePrivate': typing.Union[IncludePrivateSchema, bool, ],
        'includePending': typing.Union[IncludePendingSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query__from = api_client.QueryParameter(
    name="from",
    style=api_client.ParameterStyle.FORM,
    schema=ModelFromSchema,
    required=True,
    explode=True,
)
request_query_to = api_client.QueryParameter(
    name="to",
    style=api_client.ParameterStyle.FORM,
    schema=ToSchema,
    required=True,
    explode=True,
)
request_query_include_hourly = api_client.QueryParameter(
    name="includeHourly",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeHourlySchema,
    explode=True,
)
request_query_include_private = api_client.QueryParameter(
    name="includePrivate",
    style=api_client.ParameterStyle.FORM,
    schema=IncludePrivateSchema,
    explode=True,
)
request_query_include_pending = api_client.QueryParameter(
    name="includePending",
    style=api_client.ParameterStyle.FORM,
    schema=IncludePendingSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = RequestsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Requests


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Requests


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_whos_out_mapped_args(
        self,
        _from: date,
        to: date,
        include_hourly: typing.Optional[bool] = None,
        include_private: typing.Optional[bool] = None,
        include_pending: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if _from is not None:
            _query_params["from"] = _from
        if to is not None:
            _query_params["to"] = to
        if include_hourly is not None:
            _query_params["includeHourly"] = include_hourly
        if include_private is not None:
            _query_params["includePrivate"] = include_private
        if include_pending is not None:
            _query_params["includePending"] = include_pending
        args.query = _query_params
        return args

    async def _aget_whos_out_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Read a list of who&#x27;s out of the office.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_to,
            request_query_include_hourly,
            request_query_include_private,
            request_query_include_pending,
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
            path_template='/timeoff/whosout',
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


    def _get_whos_out_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Read a list of who&#x27;s out of the office.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_to,
            request_query_include_hourly,
            request_query_include_private,
            request_query_include_pending,
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
            path_template='/timeoff/whosout',
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


class GetWhosOutRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_whos_out(
        self,
        _from: date,
        to: date,
        include_hourly: typing.Optional[bool] = None,
        include_private: typing.Optional[bool] = None,
        include_pending: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_whos_out_mapped_args(
            _from=_from,
            to=to,
            include_hourly=include_hourly,
            include_private=include_private,
            include_pending=include_pending,
        )
        return await self._aget_whos_out_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_whos_out(
        self,
        _from: date,
        to: date,
        include_hourly: typing.Optional[bool] = None,
        include_private: typing.Optional[bool] = None,
        include_pending: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_whos_out_mapped_args(
            _from=_from,
            to=to,
            include_hourly=include_hourly,
            include_private=include_private,
            include_pending=include_pending,
        )
        return self._get_whos_out_oapg(
            query_params=args.query,
        )

class GetWhosOut(BaseApi):

    async def aget_whos_out(
        self,
        _from: date,
        to: date,
        include_hourly: typing.Optional[bool] = None,
        include_private: typing.Optional[bool] = None,
        include_pending: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> RequestsPydantic:
        raw_response = await self.raw.aget_whos_out(
            _from=_from,
            to=to,
            include_hourly=include_hourly,
            include_private=include_private,
            include_pending=include_pending,
            **kwargs,
        )
        if validate:
            return RequestsPydantic(**raw_response.body)
        return api_client.construct_model_instance(RequestsPydantic, raw_response.body)
    
    
    def get_whos_out(
        self,
        _from: date,
        to: date,
        include_hourly: typing.Optional[bool] = None,
        include_private: typing.Optional[bool] = None,
        include_pending: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> RequestsPydantic:
        raw_response = self.raw.get_whos_out(
            _from=_from,
            to=to,
            include_hourly=include_hourly,
            include_private=include_private,
            include_pending=include_pending,
        )
        if validate:
            return RequestsPydantic(**raw_response.body)
        return api_client.construct_model_instance(RequestsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        _from: date,
        to: date,
        include_hourly: typing.Optional[bool] = None,
        include_private: typing.Optional[bool] = None,
        include_pending: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_whos_out_mapped_args(
            _from=_from,
            to=to,
            include_hourly=include_hourly,
            include_private=include_private,
            include_pending=include_pending,
        )
        return await self._aget_whos_out_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        _from: date,
        to: date,
        include_hourly: typing.Optional[bool] = None,
        include_private: typing.Optional[bool] = None,
        include_pending: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_whos_out_mapped_args(
            _from=_from,
            to=to,
            include_hourly=include_hourly,
            include_private=include_private,
            include_pending=include_pending,
        )
        return self._get_whos_out_oapg(
            query_params=args.query,
        )

