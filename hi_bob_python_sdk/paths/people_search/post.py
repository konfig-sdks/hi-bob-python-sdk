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
from hi_bob_python_sdk.model.read_employees_request_reference_fields import ReadEmployeesRequestReferenceFields as ReadEmployeesRequestReferenceFieldsSchema
from hi_bob_python_sdk.model.read_employees_request_reference import ReadEmployeesRequestReference as ReadEmployeesRequestReferenceSchema
from hi_bob_python_sdk.model.employees import Employees as EmployeesSchema
from hi_bob_python_sdk.model.employee_filter import EmployeeFilter as EmployeeFilterSchema

from hi_bob_python_sdk.type.employee_filter import EmployeeFilter
from hi_bob_python_sdk.type.error import Error
from hi_bob_python_sdk.type.employees import Employees
from hi_bob_python_sdk.type.read_employees_request_reference_fields import ReadEmployeesRequestReferenceFields
from hi_bob_python_sdk.type.read_employees_request_reference import ReadEmployeesRequestReference

from ...api_client import Dictionary
from hi_bob_python_sdk.pydantic.error import Error as ErrorPydantic
from hi_bob_python_sdk.pydantic.read_employees_request_reference_fields import ReadEmployeesRequestReferenceFields as ReadEmployeesRequestReferenceFieldsPydantic
from hi_bob_python_sdk.pydantic.employee_filter import EmployeeFilter as EmployeeFilterPydantic
from hi_bob_python_sdk.pydantic.employees import Employees as EmployeesPydantic
from hi_bob_python_sdk.pydantic.read_employees_request_reference import ReadEmployeesRequestReference as ReadEmployeesRequestReferencePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = ReadEmployeesRequestReferenceSchema


request_body_read_employees_request_reference = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'Basic',
]
SchemaFor200ResponseBodyApplicationJson = EmployeesSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Employees


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Employees


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

    def _search_employees_mapped_args(
        self,
        fields: typing.Optional[ReadEmployeesRequestReferenceFields] = None,
        filters: typing.Optional[typing.List[EmployeeFilter]] = None,
        show_inactive: typing.Optional[bool] = None,
        human_readable: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if fields is not None:
            _body["fields"] = fields
        if filters is not None:
            _body["filters"] = filters
        if show_inactive is not None:
            _body["showInactive"] = show_inactive
        if human_readable is not None:
            _body["humanReadable"] = human_readable
        args.body = _body
        return args

    async def _asearch_employees_oapg(
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
        Search for employees
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
            path_template='/people/search',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_read_employees_request_reference.serialize(body, content_type)
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


    def _search_employees_oapg(
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
        Search for employees
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
            path_template='/people/search',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_read_employees_request_reference.serialize(body, content_type)
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


class SearchEmployeesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch_employees(
        self,
        fields: typing.Optional[ReadEmployeesRequestReferenceFields] = None,
        filters: typing.Optional[typing.List[EmployeeFilter]] = None,
        show_inactive: typing.Optional[bool] = None,
        human_readable: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_employees_mapped_args(
            fields=fields,
            filters=filters,
            show_inactive=show_inactive,
            human_readable=human_readable,
        )
        return await self._asearch_employees_oapg(
            body=args.body,
            **kwargs,
        )
    
    def search_employees(
        self,
        fields: typing.Optional[ReadEmployeesRequestReferenceFields] = None,
        filters: typing.Optional[typing.List[EmployeeFilter]] = None,
        show_inactive: typing.Optional[bool] = None,
        human_readable: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_employees_mapped_args(
            fields=fields,
            filters=filters,
            show_inactive=show_inactive,
            human_readable=human_readable,
        )
        return self._search_employees_oapg(
            body=args.body,
        )

class SearchEmployees(BaseApi):

    async def asearch_employees(
        self,
        fields: typing.Optional[ReadEmployeesRequestReferenceFields] = None,
        filters: typing.Optional[typing.List[EmployeeFilter]] = None,
        show_inactive: typing.Optional[bool] = None,
        human_readable: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeesPydantic:
        raw_response = await self.raw.asearch_employees(
            fields=fields,
            filters=filters,
            show_inactive=show_inactive,
            human_readable=human_readable,
            **kwargs,
        )
        if validate:
            return EmployeesPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesPydantic, raw_response.body)
    
    
    def search_employees(
        self,
        fields: typing.Optional[ReadEmployeesRequestReferenceFields] = None,
        filters: typing.Optional[typing.List[EmployeeFilter]] = None,
        show_inactive: typing.Optional[bool] = None,
        human_readable: typing.Optional[str] = None,
        validate: bool = False,
    ) -> EmployeesPydantic:
        raw_response = self.raw.search_employees(
            fields=fields,
            filters=filters,
            show_inactive=show_inactive,
            human_readable=human_readable,
        )
        if validate:
            return EmployeesPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        fields: typing.Optional[ReadEmployeesRequestReferenceFields] = None,
        filters: typing.Optional[typing.List[EmployeeFilter]] = None,
        show_inactive: typing.Optional[bool] = None,
        human_readable: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_employees_mapped_args(
            fields=fields,
            filters=filters,
            show_inactive=show_inactive,
            human_readable=human_readable,
        )
        return await self._asearch_employees_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        fields: typing.Optional[ReadEmployeesRequestReferenceFields] = None,
        filters: typing.Optional[typing.List[EmployeeFilter]] = None,
        show_inactive: typing.Optional[bool] = None,
        human_readable: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_employees_mapped_args(
            fields=fields,
            filters=filters,
            show_inactive=show_inactive,
            human_readable=human_readable,
        )
        return self._search_employees_oapg(
            body=args.body,
        )

