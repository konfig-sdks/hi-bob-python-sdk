# coding: utf-8

"""
    Bob API

    Access your employees data with the Bob API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from hi_bob_python_sdk.paths.people.post import CreateEmployeeRecord
from hi_bob_python_sdk.paths.people_id_employment.post import CreateEmploymentEntry
from hi_bob_python_sdk.paths.people_id_equities.post import CreateEquityGrant
from hi_bob_python_sdk.paths.people_id_salaries.post import CreateNewSalaryEntry
from hi_bob_python_sdk.paths.people_id_training.post import CreateTrainingRecord
from hi_bob_python_sdk.paths.people_id_variable.post import CreateVariablePayment
from hi_bob_python_sdk.paths.people_id_work.post import CreateWorkEntry
from hi_bob_python_sdk.paths.people_id_employment_entry_id.delete import DeleteEmploymentEntry
from hi_bob_python_sdk.paths.people_id_equities_entry_id.delete import DeleteEquityGrant
from hi_bob_python_sdk.paths.people_id_salaries_entry_id.delete import DeleteSalaryEntry
from hi_bob_python_sdk.paths.people_id_variable_entry_id.delete import DeleteTrainingRecord
from hi_bob_python_sdk.paths.people_id_training_entry_id.delete import DeleteTrainingRecord0
from hi_bob_python_sdk.paths.people_id_work_entry_id.delete import DeleteWorkEntry
from hi_bob_python_sdk.paths.avatars_employee_id.get import GetAvatarUrl
from hi_bob_python_sdk.paths.my_avatar.get import GetAvatarUrl0
from hi_bob_python_sdk.paths.avatars.get import GetEmailAvatar
from hi_bob_python_sdk.paths.people_id_employment.get import GetEmploymentHistory
from hi_bob_python_sdk.paths.people_id_salaries.get import GetSalaryHistory
from hi_bob_python_sdk.paths.people_id_work.get import GetWorkHistory
from hi_bob_python_sdk.paths.employees_employee_id_invitations.post import InviteEmployeeWizard
from hi_bob_python_sdk.paths.profiles.get import ListActiveEmployees
from hi_bob_python_sdk.paths.people_id_lifecycle.get import ListEmployeeLifecycle
from hi_bob_python_sdk.paths.people.get import ListEmployees
from hi_bob_python_sdk.paths.people_id_equities.get import ListEquityGrants
from hi_bob_python_sdk.paths.people_id_training.get import ListTrainingRecords
from hi_bob_python_sdk.paths.people_id_variable.get import ListVariablePayments
from hi_bob_python_sdk.paths.people_identifier.get import ReadEmployeeById
from hi_bob_python_sdk.paths.people_identifier.post import ReadEmployeeFields
from hi_bob_python_sdk.paths.employees_identifier_uninvite.post import RevokeAccessToEmployee
from hi_bob_python_sdk.paths.people_search.post import SearchEmployees
from hi_bob_python_sdk.paths.employees_employee_id_start_date.post import SetStartDate
from hi_bob_python_sdk.paths.employees_identifier_terminate.post import TerminateEmployee
from hi_bob_python_sdk.paths.people_id_email.put import UpdateEmail
from hi_bob_python_sdk.paths.people_identifier.put import UpdateEmployeeRecord
from hi_bob_python_sdk.paths.people_id_employment_entry_id.put import UpdateEmploymentEntry
from hi_bob_python_sdk.paths.people_id_equities_entry_id.put import UpdateEquityGrantForEmployee
from hi_bob_python_sdk.paths.people_id_work_entry_id.put import UpdateWorkEntry
from hi_bob_python_sdk.paths.avatars_employee_id.put import UploadEmployeeAvatarUrl
from hi_bob_python_sdk.apis.tags.people_api_raw import PeopleApiRaw


class PeopleApi(
    CreateEmployeeRecord,
    CreateEmploymentEntry,
    CreateEquityGrant,
    CreateNewSalaryEntry,
    CreateTrainingRecord,
    CreateVariablePayment,
    CreateWorkEntry,
    DeleteEmploymentEntry,
    DeleteEquityGrant,
    DeleteSalaryEntry,
    DeleteTrainingRecord,
    DeleteTrainingRecord0,
    DeleteWorkEntry,
    GetAvatarUrl,
    GetAvatarUrl0,
    GetEmailAvatar,
    GetEmploymentHistory,
    GetSalaryHistory,
    GetWorkHistory,
    InviteEmployeeWizard,
    ListActiveEmployees,
    ListEmployeeLifecycle,
    ListEmployees,
    ListEquityGrants,
    ListTrainingRecords,
    ListVariablePayments,
    ReadEmployeeById,
    ReadEmployeeFields,
    RevokeAccessToEmployee,
    SearchEmployees,
    SetStartDate,
    TerminateEmployee,
    UpdateEmail,
    UpdateEmployeeRecord,
    UpdateEmploymentEntry,
    UpdateEquityGrantForEmployee,
    UpdateWorkEntry,
    UploadEmployeeAvatarUrl,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PeopleApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PeopleApiRaw(api_client)
