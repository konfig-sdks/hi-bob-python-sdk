# coding: utf-8

"""
    Bob API

    Access your employees data with the Bob API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from hi_bob_python_sdk.paths.company_people_fields.post import AddNewField
from hi_bob_python_sdk.paths.company_named_lists_list_name.post import AddNewItemToNamedList
from hi_bob_python_sdk.paths.company_people_fields_field_id.delete import DeleteField
from hi_bob_python_sdk.paths.company_named_lists_list_name_item_id.delete import DeleteItemFromCompanyNamedList
from hi_bob_python_sdk.paths.company_people_fields.get import GetCompanyFields
from hi_bob_python_sdk.paths.company_named_lists.get import GetCompanyNamedLists
from hi_bob_python_sdk.paths.people_custom_tables_metadata.get import GetCustomTableMetadata
from hi_bob_python_sdk.paths.company_named_lists_list_name.get import GetNamedList
from hi_bob_python_sdk.paths.metadata_objects_position.get import GetPositionFields
from hi_bob_python_sdk.paths.people_custom_tables_metadata_custom_table_id.get import GetTableDetails
from hi_bob_python_sdk.paths.company_people_fields_field_id.put import UpdateField
from hi_bob_python_sdk.paths.company_named_lists_list_name_item_id.put import UpdateItemFromNamedList
from hi_bob_python_sdk.apis.tags.metadata_api_raw import MetadataApiRaw


class MetadataApi(
    AddNewField,
    AddNewItemToNamedList,
    DeleteField,
    DeleteItemFromCompanyNamedList,
    GetCompanyFields,
    GetCompanyNamedLists,
    GetCustomTableMetadata,
    GetNamedList,
    GetPositionFields,
    GetTableDetails,
    UpdateField,
    UpdateItemFromNamedList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MetadataApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MetadataApiRaw(api_client)