# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_get_request(
    management_group_id: str,
    name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-01-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}')
    path_format_arguments = {
        "managementGroupId": _SERIALIZER.url("management_group_id", management_group_id, 'str', skip_quote=True),
        "name": _SERIALIZER.url("name", name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_request(
    management_group_id: str,
    name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2020-01-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}')
    path_format_arguments = {
        "managementGroupId": _SERIALIZER.url("management_group_id", management_group_id, 'str', skip_quote=True),
        "name": _SERIALIZER.url("name", name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request(
    management_group_id: str,
    name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-01-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}')
    path_format_arguments = {
        "managementGroupId": _SERIALIZER.url("management_group_id", management_group_id, 'str', skip_quote=True),
        "name": _SERIALIZER.url("name", name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    management_group_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-01-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings')
    path_format_arguments = {
        "managementGroupId": _SERIALIZER.url("management_group_id", management_group_id, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class ManagementGroupDiagnosticSettingsOperations(object):
    """ManagementGroupDiagnosticSettingsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~$(python-base-namespace).v2020_01_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get(
        self,
        management_group_id: str,
        name: str,
        **kwargs: Any
    ) -> "_models.ManagementGroupDiagnosticSettingsResource":
        """Gets the active management group diagnostic settings for the specified resource.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagementGroupDiagnosticSettingsResource, or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ManagementGroupDiagnosticSettingsResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            management_group_id=management_group_id,
            name=name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagementGroupDiagnosticSettingsResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}'}  # type: ignore


    @distributed_trace
    def create_or_update(
        self,
        management_group_id: str,
        name: str,
        parameters: "_models.ManagementGroupDiagnosticSettingsResource",
        **kwargs: Any
    ) -> "_models.ManagementGroupDiagnosticSettingsResource":
        """Creates or updates management group diagnostic settings for the specified resource.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :param parameters: Parameters supplied to the operation.
        :type parameters:
         ~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagementGroupDiagnosticSettingsResource, or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ManagementGroupDiagnosticSettingsResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ManagementGroupDiagnosticSettingsResource')

        request = build_create_or_update_request(
            management_group_id=management_group_id,
            name=name,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagementGroupDiagnosticSettingsResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        management_group_id: str,
        name: str,
        **kwargs: Any
    ) -> None:
        """Deletes existing management group diagnostic settings for the specified resource.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            management_group_id=management_group_id,
            name=name,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        management_group_id: str,
        **kwargs: Any
    ) -> Iterable["_models.ManagementGroupDiagnosticSettingsResourceCollection"]:
        """Gets the active management group diagnostic settings list for the specified management group.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either
         ManagementGroupDiagnosticSettingsResourceCollection or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResourceCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ManagementGroupDiagnosticSettingsResourceCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    management_group_id=management_group_id,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    management_group_id=management_group_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ManagementGroupDiagnosticSettingsResourceCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings'}  # type: ignore
