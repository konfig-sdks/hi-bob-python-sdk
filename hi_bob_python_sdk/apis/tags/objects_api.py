# coding: utf-8

"""
    Bob API

    Access your employees data with the Bob API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from hi_bob_python_sdk.paths.objects_position_search.post import SearchCompanyPositions
from hi_bob_python_sdk.apis.tags.objects_api_raw import ObjectsApiRaw


class ObjectsApi(
    SearchCompanyPositions,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ObjectsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ObjectsApiRaw(api_client)