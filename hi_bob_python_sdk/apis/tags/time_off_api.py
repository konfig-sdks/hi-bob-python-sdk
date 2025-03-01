# coding: utf-8

"""
    Bob API

    Access your employees data with the Bob API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from hi_bob_python_sdk.paths.timeoff_policy_types_policy_type_reason_codes.post import AddReasonCodes
from hi_bob_python_sdk.paths.timeoff_employees_id_requests_request_id.delete import CancelRequest
from hi_bob_python_sdk.paths.timeoff_employees_id_adjustments.post import CreateBalanceAdjustment
from hi_bob_python_sdk.paths.timeoff_employees_id_requests_request_id.get import GetDetailsOfRequest
from hi_bob_python_sdk.paths.timeoff_employees_id_balance.get import GetEmployeeBalance
from hi_bob_python_sdk.paths.timeoff_requests_changes.get import GetNewDeletedRequestsSinceDate
from hi_bob_python_sdk.paths.timeoff_outtoday.get import GetOutOfOffice
from hi_bob_python_sdk.paths.timeoff_policy_types_policy_type.get import GetPolicyDetails
from hi_bob_python_sdk.paths.timeoff_policies.get import GetPolicyDetails0
from hi_bob_python_sdk.paths.timeoff_whosout.get import GetWhosOut
from hi_bob_python_sdk.paths.timeoff_policies_names.get import ListPolicyTypeNames
from hi_bob_python_sdk.paths.timeoff_policy_types.get import ListPolicyTypesNames
from hi_bob_python_sdk.paths.timeoff_policy_types_policy_type_reason_codes.get import ListReasonCodes
from hi_bob_python_sdk.paths.timeoff_employees_id_requests.post import SubmitNewRequest
from hi_bob_python_sdk.paths.timeoff_employees_id_diff_hours_requests.post import SubmitNewRequestDiffHours
from hi_bob_python_sdk.apis.tags.time_off_api_raw import TimeOffApiRaw


class TimeOffApi(
    AddReasonCodes,
    CancelRequest,
    CreateBalanceAdjustment,
    GetDetailsOfRequest,
    GetEmployeeBalance,
    GetNewDeletedRequestsSinceDate,
    GetOutOfOffice,
    GetPolicyDetails,
    GetPolicyDetails0,
    GetWhosOut,
    ListPolicyTypeNames,
    ListPolicyTypesNames,
    ListReasonCodes,
    SubmitNewRequest,
    SubmitNewRequestDiffHours,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TimeOffApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TimeOffApiRaw(api_client)
