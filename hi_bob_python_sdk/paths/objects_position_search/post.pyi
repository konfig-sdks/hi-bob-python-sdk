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
from hi_bob_python_sdk.model.position_entries import PositionEntries as PositionEntriesSchema
from hi_bob_python_sdk.model.get_positions_request_fields import GetPositionsRequestFields as GetPositionsRequestFieldsSchema
from hi_bob_python_sdk.model.filter_instruction import FilterInstruction as FilterInstructionSchema
from hi_bob_python_sdk.model.get_positions_request import GetPositionsRequest as GetPositionsRequestSchema

from hi_bob_python_sdk.type.get_positions_request import GetPositionsRequest
from hi_bob_python_sdk.type.error import Error
from hi_bob_python_sdk.type.position_entries import PositionEntries
from hi_bob_python_sdk.type.get_positions_request_fields import GetPositionsRequestFields
from hi_bob_python_sdk.type.filter_instruction import FilterInstruction

from ...api_client import Dictionary
from hi_bob_python_sdk.pydantic.get_positions_request_fields import GetPositionsRequestFields as GetPositionsRequestFieldsPydantic
from hi_bob_python_sdk.pydantic.get_positions_request import GetPositionsRequest as GetPositionsRequestPydantic
from hi_bob_python_sdk.pydantic.filter_instruction import FilterInstruction as FilterInstructionPydantic
from hi_bob_python_sdk.pydantic.error import Error as ErrorPydantic
from hi_bob_python_sdk.pydantic.position_entries import PositionEntries as PositionEntriesPydantic

# body param
SchemaForRequestBodyApplicationJson = GetPositionsRequestSchema


request_body_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = PositionEntriesSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PositionEntries


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PositionEntries


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

    def _search_company_positions_mapped_args(
        self,
        fields: GetPositionsRequestFields,
        filters: typing.List[FilterInstruction],
        include_human_readable: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if fields is not None:
            _body["fields"] = fields
        if filters is not None:
            _body["filters"] = filters
        if include_human_readable is not None:
            _body["includeHumanReadable"] = include_human_readable
        args.body = _body
        return args

    async def _asearch_company_positions_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Read company positions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/objects/position/search',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_body.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _search_company_positions_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Read company positions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/objects/position/search',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_body.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class SearchCompanyPositionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch_company_positions(
        self,
        fields: GetPositionsRequestFields,
        filters: typing.List[FilterInstruction],
        include_human_readable: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_company_positions_mapped_args(
            fields=fields,
            filters=filters,
            include_human_readable=include_human_readable,
        )
        return await self._asearch_company_positions_oapg(
            body=args.body,
            **kwargs,
        )
    
    def search_company_positions(
        self,
        fields: GetPositionsRequestFields,
        filters: typing.List[FilterInstruction],
        include_human_readable: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_company_positions_mapped_args(
            fields=fields,
            filters=filters,
            include_human_readable=include_human_readable,
        )
        return self._search_company_positions_oapg(
            body=args.body,
        )

class SearchCompanyPositions(BaseApi):

    async def asearch_company_positions(
        self,
        fields: GetPositionsRequestFields,
        filters: typing.List[FilterInstruction],
        include_human_readable: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> PositionEntriesPydantic:
        raw_response = await self.raw.asearch_company_positions(
            fields=fields,
            filters=filters,
            include_human_readable=include_human_readable,
            **kwargs,
        )
        if validate:
            return RootModel[PositionEntriesPydantic](raw_response.body).root
        return api_client.construct_model_instance(PositionEntriesPydantic, raw_response.body)
    
    
    def search_company_positions(
        self,
        fields: GetPositionsRequestFields,
        filters: typing.List[FilterInstruction],
        include_human_readable: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> PositionEntriesPydantic:
        raw_response = self.raw.search_company_positions(
            fields=fields,
            filters=filters,
            include_human_readable=include_human_readable,
        )
        if validate:
            return RootModel[PositionEntriesPydantic](raw_response.body).root
        return api_client.construct_model_instance(PositionEntriesPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        fields: GetPositionsRequestFields,
        filters: typing.List[FilterInstruction],
        include_human_readable: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_company_positions_mapped_args(
            fields=fields,
            filters=filters,
            include_human_readable=include_human_readable,
        )
        return await self._asearch_company_positions_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        fields: GetPositionsRequestFields,
        filters: typing.List[FilterInstruction],
        include_human_readable: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_company_positions_mapped_args(
            fields=fields,
            filters=filters,
            include_human_readable=include_human_readable,
        )
        return self._search_company_positions_oapg(
            body=args.body,
        )

