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

from hi_bob_python_sdk.model.employment_entry import EmploymentEntry as EmploymentEntrySchema

from hi_bob_python_sdk.type.employment_entry import EmploymentEntry

from ...api_client import Dictionary
from hi_bob_python_sdk.pydantic.employment_entry import EmploymentEntry as EmploymentEntryPydantic

# Path params
IdSchema = schemas.StrSchema
EntryIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
        'entry_id': typing.Union[EntryIdSchema, decimal.Decimal, int, ],
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


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
request_path_entry_id = api_client.PathParameter(
    name="entry_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EntryIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = EmploymentEntrySchema


request_body_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: 


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)


class BaseApi(api_client.Api):

    def _update_employment_entry_mapped_args(
        self,
        effective_date: date,
        id: str,
        entry_id: int,
        id: typing.Optional[int] = None,
        reason: typing.Optional[str] = None,
        contract: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        salary_pay_type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if id is not None:
            _body["id"] = id
        if reason is not None:
            _body["reason"] = reason
        if effective_date is not None:
            _body["effectiveDate"] = effective_date
        if contract is not None:
            _body["contract"] = contract
        if type is not None:
            _body["type"] = type
        if salary_pay_type is not None:
            _body["salaryPayType"] = salary_pay_type
        args.body = _body
        if id is not None:
            _path_params["id"] = id
        if entry_id is not None:
            _path_params["entry_id"] = entry_id
        args.path = _path_params
        return args

    async def _aupdate_employment_entry_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Updates an employment entry from a given employee&#x27;s employment history.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
            request_path_entry_id,
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
        method = 'put'.upper()
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
            path_template='/people/{id}/employment/{entry_id}',
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
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


    def _update_employment_entry_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Updates an employment entry from a given employee&#x27;s employment history.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
            request_path_entry_id,
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
        method = 'put'.upper()
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
            path_template='/people/{id}/employment/{entry_id}',
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateEmploymentEntryRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_employment_entry(
        self,
        effective_date: date,
        id: str,
        entry_id: int,
        id: typing.Optional[int] = None,
        reason: typing.Optional[str] = None,
        contract: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        salary_pay_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_employment_entry_mapped_args(
            body=body,
            effective_date=effective_date,
            id=id,
            entry_id=entry_id,
            id=id,
            reason=reason,
            contract=contract,
            type=type,
            salary_pay_type=salary_pay_type,
        )
        return await self._aupdate_employment_entry_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_employment_entry(
        self,
        effective_date: date,
        id: str,
        entry_id: int,
        id: typing.Optional[int] = None,
        reason: typing.Optional[str] = None,
        contract: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        salary_pay_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_employment_entry_mapped_args(
            body=body,
            effective_date=effective_date,
            id=id,
            entry_id=entry_id,
            id=id,
            reason=reason,
            contract=contract,
            type=type,
            salary_pay_type=salary_pay_type,
        )
        return self._update_employment_entry_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateEmploymentEntry(BaseApi):

    async def aupdate_employment_entry(
        self,
        effective_date: date,
        id: str,
        entry_id: int,
        id: typing.Optional[int] = None,
        reason: typing.Optional[str] = None,
        contract: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        salary_pay_type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_employment_entry(
            body=body,
            effective_date=effective_date,
            id=id,
            entry_id=entry_id,
            id=id,
            reason=reason,
            contract=contract,
            type=type,
            salary_pay_type=salary_pay_type,
            **kwargs,
        )
    
    
    def update_employment_entry(
        self,
        effective_date: date,
        id: str,
        entry_id: int,
        id: typing.Optional[int] = None,
        reason: typing.Optional[str] = None,
        contract: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        salary_pay_type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_employment_entry(
            body=body,
            effective_date=effective_date,
            id=id,
            entry_id=entry_id,
            id=id,
            reason=reason,
            contract=contract,
            type=type,
            salary_pay_type=salary_pay_type,
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        effective_date: date,
        id: str,
        entry_id: int,
        id: typing.Optional[int] = None,
        reason: typing.Optional[str] = None,
        contract: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        salary_pay_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_employment_entry_mapped_args(
            body=body,
            effective_date=effective_date,
            id=id,
            entry_id=entry_id,
            id=id,
            reason=reason,
            contract=contract,
            type=type,
            salary_pay_type=salary_pay_type,
        )
        return await self._aupdate_employment_entry_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        effective_date: date,
        id: str,
        entry_id: int,
        id: typing.Optional[int] = None,
        reason: typing.Optional[str] = None,
        contract: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        salary_pay_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_employment_entry_mapped_args(
            body=body,
            effective_date=effective_date,
            id=id,
            entry_id=entry_id,
            id=id,
            reason=reason,
            contract=contract,
            type=type,
            salary_pay_type=salary_pay_type,
        )
        return self._update_employment_entry_oapg(
            body=args.body,
            path_params=args.path,
        )

