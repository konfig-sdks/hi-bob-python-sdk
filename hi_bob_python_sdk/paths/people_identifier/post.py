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
from hi_bob_python_sdk.model.read_single_employee_request_reference import ReadSingleEmployeeRequestReference as ReadSingleEmployeeRequestReferenceSchema
from hi_bob_python_sdk.model.read_single_employee_request_reference_fields import ReadSingleEmployeeRequestReferenceFields as ReadSingleEmployeeRequestReferenceFieldsSchema
from hi_bob_python_sdk.model.employees import Employees as EmployeesSchema

from hi_bob_python_sdk.type.read_single_employee_request_reference import ReadSingleEmployeeRequestReference
from hi_bob_python_sdk.type.error import Error
from hi_bob_python_sdk.type.read_single_employee_request_reference_fields import ReadSingleEmployeeRequestReferenceFields
from hi_bob_python_sdk.type.employees import Employees

from ...api_client import Dictionary
from hi_bob_python_sdk.pydantic.read_single_employee_request_reference_fields import ReadSingleEmployeeRequestReferenceFields as ReadSingleEmployeeRequestReferenceFieldsPydantic
from hi_bob_python_sdk.pydantic.error import Error as ErrorPydantic
from hi_bob_python_sdk.pydantic.read_single_employee_request_reference import ReadSingleEmployeeRequestReference as ReadSingleEmployeeRequestReferencePydantic
from hi_bob_python_sdk.pydantic.employees import Employees as EmployeesPydantic

from . import path

# Path params
IdentifierSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'identifier': typing.Union[IdentifierSchema, str, ],
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


request_path_identifier = api_client.PathParameter(
    name="identifier",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdentifierSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ReadSingleEmployeeRequestReferenceSchema


request_body_read_single_employee_request_reference = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
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

    def _read_employee_fields_mapped_args(
        self,
        identifier: str,
        fields: typing.Optional[ReadSingleEmployeeRequestReferenceFields] = None,
        human_readable: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if fields is not None:
            _body["fields"] = fields
        if human_readable is not None:
            _body["humanReadable"] = human_readable
        args.body = _body
        if identifier is not None:
            _path_params["identifier"] = identifier
        args.path = _path_params
        return args

    async def _aread_employee_fields_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Read company employee fields by employee ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_identifier,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/people/{identifier}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_read_single_employee_request_reference.serialize(body, content_type)
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


    def _read_employee_fields_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Read company employee fields by employee ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_identifier,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/people/{identifier}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_read_single_employee_request_reference.serialize(body, content_type)
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


class ReadEmployeeFieldsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aread_employee_fields(
        self,
        identifier: str,
        fields: typing.Optional[ReadSingleEmployeeRequestReferenceFields] = None,
        human_readable: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._read_employee_fields_mapped_args(
            identifier=identifier,
            fields=fields,
            human_readable=human_readable,
        )
        return await self._aread_employee_fields_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def read_employee_fields(
        self,
        identifier: str,
        fields: typing.Optional[ReadSingleEmployeeRequestReferenceFields] = None,
        human_readable: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._read_employee_fields_mapped_args(
            identifier=identifier,
            fields=fields,
            human_readable=human_readable,
        )
        return self._read_employee_fields_oapg(
            body=args.body,
            path_params=args.path,
        )

class ReadEmployeeFields(BaseApi):

    async def aread_employee_fields(
        self,
        identifier: str,
        fields: typing.Optional[ReadSingleEmployeeRequestReferenceFields] = None,
        human_readable: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeesPydantic:
        raw_response = await self.raw.aread_employee_fields(
            identifier=identifier,
            fields=fields,
            human_readable=human_readable,
            **kwargs,
        )
        if validate:
            return EmployeesPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesPydantic, raw_response.body)
    
    
    def read_employee_fields(
        self,
        identifier: str,
        fields: typing.Optional[ReadSingleEmployeeRequestReferenceFields] = None,
        human_readable: typing.Optional[str] = None,
        validate: bool = False,
    ) -> EmployeesPydantic:
        raw_response = self.raw.read_employee_fields(
            identifier=identifier,
            fields=fields,
            human_readable=human_readable,
        )
        if validate:
            return EmployeesPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        identifier: str,
        fields: typing.Optional[ReadSingleEmployeeRequestReferenceFields] = None,
        human_readable: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._read_employee_fields_mapped_args(
            identifier=identifier,
            fields=fields,
            human_readable=human_readable,
        )
        return await self._aread_employee_fields_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        identifier: str,
        fields: typing.Optional[ReadSingleEmployeeRequestReferenceFields] = None,
        human_readable: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._read_employee_fields_mapped_args(
            identifier=identifier,
            fields=fields,
            human_readable=human_readable,
        )
        return self._read_employee_fields_oapg(
            body=args.body,
            path_params=args.path,
        )

