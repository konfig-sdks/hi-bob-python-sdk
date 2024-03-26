import typing_extensions

from hi_bob_python_sdk.paths import PathValues
from hi_bob_python_sdk.apis.paths.people_search import PeopleSearch
from hi_bob_python_sdk.apis.paths.people import People
from hi_bob_python_sdk.apis.paths.people_identifier import PeopleIdentifier
from hi_bob_python_sdk.apis.paths.employees_identifier_uninvite import EmployeesIdentifierUninvite
from hi_bob_python_sdk.apis.paths.employees_identifier_terminate import EmployeesIdentifierTerminate
from hi_bob_python_sdk.apis.paths.onboarding_wizards import OnboardingWizards
from hi_bob_python_sdk.apis.paths.employees_employee_id_invitations import EmployeesEmployeeIdInvitations
from hi_bob_python_sdk.apis.paths.employees_employee_id_start_date import EmployeesEmployeeIdStartDate
from hi_bob_python_sdk.apis.paths.company_reports import CompanyReports
from hi_bob_python_sdk.apis.paths.company_reports_report_id_download import CompanyReportsReportIdDownload
from hi_bob_python_sdk.apis.paths.company_reports_report_id_download_async import CompanyReportsReportIdDownloadAsync
from hi_bob_python_sdk.apis.paths.company_reports_download_report_name import CompanyReportsDownloadReportName
from hi_bob_python_sdk.apis.paths.profiles import Profiles
from hi_bob_python_sdk.apis.paths.avatars import Avatars
from hi_bob_python_sdk.apis.paths.avatars_employee_id import AvatarsEmployeeId
from hi_bob_python_sdk.apis.paths.my_avatar import MyAvatar
from hi_bob_python_sdk.apis.paths.tasks import Tasks
from hi_bob_python_sdk.apis.paths.my_tasks import MyTasks
from hi_bob_python_sdk.apis.paths.tasks_people_id import TasksPeopleId
from hi_bob_python_sdk.apis.paths.tasks_task_id_complete import TasksTaskIdComplete
from hi_bob_python_sdk.apis.paths.people_id_email import PeopleIdEmail
from hi_bob_python_sdk.apis.paths.company_named_lists import CompanyNamedLists
from hi_bob_python_sdk.apis.paths.company_named_lists_list_name import CompanyNamedListsListName
from hi_bob_python_sdk.apis.paths.company_named_lists_list_name_item_id import CompanyNamedListsListNameItemId
from hi_bob_python_sdk.apis.paths.company_people_fields import CompanyPeopleFields
from hi_bob_python_sdk.apis.paths.company_people_fields_field_id import CompanyPeopleFieldsFieldId
from hi_bob_python_sdk.apis.paths.timeoff_employees_id_requests import TimeoffEmployeesIdRequests
from hi_bob_python_sdk.apis.paths.timeoff_employees_id_diff_hours_requests import TimeoffEmployeesIdDiffHoursRequests
from hi_bob_python_sdk.apis.paths.timeoff_employees_id_requests_request_id import TimeoffEmployeesIdRequestsRequestId
from hi_bob_python_sdk.apis.paths.timeoff_requests_changes import TimeoffRequestsChanges
from hi_bob_python_sdk.apis.paths.timeoff_whosout import TimeoffWhosout
from hi_bob_python_sdk.apis.paths.timeoff_outtoday import TimeoffOuttoday
from hi_bob_python_sdk.apis.paths.timeoff_policy_types_policy_type_reason_codes import TimeoffPolicyTypesPolicyTypeReasonCodes
from hi_bob_python_sdk.apis.paths.timeoff_policy_types_policy_type import TimeoffPolicyTypesPolicyType
from hi_bob_python_sdk.apis.paths.timeoff_policy_types import TimeoffPolicyTypes
from hi_bob_python_sdk.apis.paths.timeoff_policies import TimeoffPolicies
from hi_bob_python_sdk.apis.paths.timeoff_policies_names import TimeoffPoliciesNames
from hi_bob_python_sdk.apis.paths.timeoff_employees_id_balance import TimeoffEmployeesIdBalance
from hi_bob_python_sdk.apis.paths.timeoff_employees_id_adjustments import TimeoffEmployeesIdAdjustments
from hi_bob_python_sdk.apis.paths.attendance_import_import_method import AttendanceImportImportMethod
from hi_bob_python_sdk.apis.paths.payroll_history import PayrollHistory
from hi_bob_python_sdk.apis.paths.docs_people_id_shared import DocsPeopleIdShared
from hi_bob_python_sdk.apis.paths.docs_people_id_confidential import DocsPeopleIdConfidential
from hi_bob_python_sdk.apis.paths.docs_people_id_shared_upload import DocsPeopleIdSharedUpload
from hi_bob_python_sdk.apis.paths.docs_people_id_confidential_upload import DocsPeopleIdConfidentialUpload
from hi_bob_python_sdk.apis.paths.docs_people_id_shared_doc_id import DocsPeopleIdSharedDocId
from hi_bob_python_sdk.apis.paths.docs_people_id_confidential_doc_id import DocsPeopleIdConfidentialDocId
from hi_bob_python_sdk.apis.paths.docs_people_id import DocsPeopleId
from hi_bob_python_sdk.apis.paths.people_id_work import PeopleIdWork
from hi_bob_python_sdk.apis.paths.people_id_work_entry_id import PeopleIdWorkEntryId
from hi_bob_python_sdk.apis.paths.people_id_employment import PeopleIdEmployment
from hi_bob_python_sdk.apis.paths.people_id_employment_entry_id import PeopleIdEmploymentEntryId
from hi_bob_python_sdk.apis.paths.people_id_lifecycle import PeopleIdLifecycle
from hi_bob_python_sdk.apis.paths.people_id_salaries import PeopleIdSalaries
from hi_bob_python_sdk.apis.paths.people_id_salaries_entry_id import PeopleIdSalariesEntryId
from hi_bob_python_sdk.apis.paths.people_id_equities import PeopleIdEquities
from hi_bob_python_sdk.apis.paths.people_id_equities_entry_id import PeopleIdEquitiesEntryId
from hi_bob_python_sdk.apis.paths.people_id_variable import PeopleIdVariable
from hi_bob_python_sdk.apis.paths.people_id_variable_entry_id import PeopleIdVariableEntryId
from hi_bob_python_sdk.apis.paths.people_id_training import PeopleIdTraining
from hi_bob_python_sdk.apis.paths.people_id_training_entry_id import PeopleIdTrainingEntryId
from hi_bob_python_sdk.apis.paths.people_custom_tables_metadata import PeopleCustomTablesMetadata
from hi_bob_python_sdk.apis.paths.people_custom_tables_metadata_custom_table_id import PeopleCustomTablesMetadataCustomTableId
from hi_bob_python_sdk.apis.paths.people_custom_tables_employee_id_custom_table_id import PeopleCustomTablesEmployeeIdCustomTableId
from hi_bob_python_sdk.apis.paths.people_custom_tables_employee_id_custom_table_id_entry_id import PeopleCustomTablesEmployeeIdCustomTableIdEntryId
from hi_bob_python_sdk.apis.paths.metadata_objects_position import MetadataObjectsPosition
from hi_bob_python_sdk.apis.paths.objects_position_search import ObjectsPositionSearch

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PEOPLE_SEARCH: PeopleSearch,
        PathValues.PEOPLE: People,
        PathValues.PEOPLE_IDENTIFIER: PeopleIdentifier,
        PathValues.EMPLOYEES_IDENTIFIER_UNINVITE: EmployeesIdentifierUninvite,
        PathValues.EMPLOYEES_IDENTIFIER_TERMINATE: EmployeesIdentifierTerminate,
        PathValues.ONBOARDING_WIZARDS: OnboardingWizards,
        PathValues.EMPLOYEES_EMPLOYEE_ID_INVITATIONS: EmployeesEmployeeIdInvitations,
        PathValues.EMPLOYEES_EMPLOYEE_ID_STARTDATE: EmployeesEmployeeIdStartDate,
        PathValues.COMPANY_REPORTS: CompanyReports,
        PathValues.COMPANY_REPORTS_REPORT_ID_DOWNLOAD: CompanyReportsReportIdDownload,
        PathValues.COMPANY_REPORTS_REPORT_ID_DOWNLOADASYNC: CompanyReportsReportIdDownloadAsync,
        PathValues.COMPANY_REPORTS_DOWNLOAD_REPORT_NAME: CompanyReportsDownloadReportName,
        PathValues.PROFILES: Profiles,
        PathValues.AVATARS: Avatars,
        PathValues.AVATARS_EMPLOYEE_ID: AvatarsEmployeeId,
        PathValues.MY_AVATAR: MyAvatar,
        PathValues.TASKS: Tasks,
        PathValues.MY_TASKS: MyTasks,
        PathValues.TASKS_PEOPLE_ID: TasksPeopleId,
        PathValues.TASKS_TASK_ID_COMPLETE: TasksTaskIdComplete,
        PathValues.PEOPLE_ID_EMAIL: PeopleIdEmail,
        PathValues.COMPANY_NAMEDLISTS: CompanyNamedLists,
        PathValues.COMPANY_NAMEDLISTS_LIST_NAME: CompanyNamedListsListName,
        PathValues.COMPANY_NAMEDLISTS_LIST_NAME_ITEM_ID: CompanyNamedListsListNameItemId,
        PathValues.COMPANY_PEOPLE_FIELDS: CompanyPeopleFields,
        PathValues.COMPANY_PEOPLE_FIELDS_FIELD_ID: CompanyPeopleFieldsFieldId,
        PathValues.TIMEOFF_EMPLOYEES_ID_REQUESTS: TimeoffEmployeesIdRequests,
        PathValues.TIMEOFF_EMPLOYEES_ID_DIFF_HOURS_REQUESTS: TimeoffEmployeesIdDiffHoursRequests,
        PathValues.TIMEOFF_EMPLOYEES_ID_REQUESTS_REQUEST_ID: TimeoffEmployeesIdRequestsRequestId,
        PathValues.TIMEOFF_REQUESTS_CHANGES: TimeoffRequestsChanges,
        PathValues.TIMEOFF_WHOSOUT: TimeoffWhosout,
        PathValues.TIMEOFF_OUTTODAY: TimeoffOuttoday,
        PathValues.TIMEOFF_POLICYTYPES_POLICY_TYPE_REASONCODES: TimeoffPolicyTypesPolicyTypeReasonCodes,
        PathValues.TIMEOFF_POLICYTYPES_POLICY_TYPE: TimeoffPolicyTypesPolicyType,
        PathValues.TIMEOFF_POLICYTYPES: TimeoffPolicyTypes,
        PathValues.TIMEOFF_POLICIES: TimeoffPolicies,
        PathValues.TIMEOFF_POLICIES_NAMES: TimeoffPoliciesNames,
        PathValues.TIMEOFF_EMPLOYEES_ID_BALANCE: TimeoffEmployeesIdBalance,
        PathValues.TIMEOFF_EMPLOYEES_ID_ADJUSTMENTS: TimeoffEmployeesIdAdjustments,
        PathValues.ATTENDANCE_IMPORT_IMPORT_METHOD: AttendanceImportImportMethod,
        PathValues.PAYROLL_HISTORY: PayrollHistory,
        PathValues.DOCS_PEOPLE_ID_SHARED: DocsPeopleIdShared,
        PathValues.DOCS_PEOPLE_ID_CONFIDENTIAL: DocsPeopleIdConfidential,
        PathValues.DOCS_PEOPLE_ID_SHARED_UPLOAD: DocsPeopleIdSharedUpload,
        PathValues.DOCS_PEOPLE_ID_CONFIDENTIAL_UPLOAD: DocsPeopleIdConfidentialUpload,
        PathValues.DOCS_PEOPLE_ID_SHARED_DOC_ID: DocsPeopleIdSharedDocId,
        PathValues.DOCS_PEOPLE_ID_CONFIDENTIAL_DOC_ID: DocsPeopleIdConfidentialDocId,
        PathValues.DOCS_PEOPLE_ID: DocsPeopleId,
        PathValues.PEOPLE_ID_WORK: PeopleIdWork,
        PathValues.PEOPLE_ID_WORK_ENTRY_ID: PeopleIdWorkEntryId,
        PathValues.PEOPLE_ID_EMPLOYMENT: PeopleIdEmployment,
        PathValues.PEOPLE_ID_EMPLOYMENT_ENTRY_ID: PeopleIdEmploymentEntryId,
        PathValues.PEOPLE_ID_LIFECYCLE: PeopleIdLifecycle,
        PathValues.PEOPLE_ID_SALARIES: PeopleIdSalaries,
        PathValues.PEOPLE_ID_SALARIES_ENTRY_ID: PeopleIdSalariesEntryId,
        PathValues.PEOPLE_ID_EQUITIES: PeopleIdEquities,
        PathValues.PEOPLE_ID_EQUITIES_ENTRY_ID: PeopleIdEquitiesEntryId,
        PathValues.PEOPLE_ID_VARIABLE: PeopleIdVariable,
        PathValues.PEOPLE_ID_VARIABLE_ENTRY_ID: PeopleIdVariableEntryId,
        PathValues.PEOPLE_ID_TRAINING: PeopleIdTraining,
        PathValues.PEOPLE_ID_TRAINING_ENTRY_ID: PeopleIdTrainingEntryId,
        PathValues.PEOPLE_CUSTOMTABLES_METADATA: PeopleCustomTablesMetadata,
        PathValues.PEOPLE_CUSTOMTABLES_METADATA_CUSTOM_TABLE_ID: PeopleCustomTablesMetadataCustomTableId,
        PathValues.PEOPLE_CUSTOMTABLES_EMPLOYEE_ID_CUSTOM_TABLE_ID: PeopleCustomTablesEmployeeIdCustomTableId,
        PathValues.PEOPLE_CUSTOMTABLES_EMPLOYEE_ID_CUSTOM_TABLE_ID_ENTRY_ID: PeopleCustomTablesEmployeeIdCustomTableIdEntryId,
        PathValues.METADATA_OBJECTS_POSITION: MetadataObjectsPosition,
        PathValues.OBJECTS_POSITION_SEARCH: ObjectsPositionSearch,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PEOPLE_SEARCH: PeopleSearch,
        PathValues.PEOPLE: People,
        PathValues.PEOPLE_IDENTIFIER: PeopleIdentifier,
        PathValues.EMPLOYEES_IDENTIFIER_UNINVITE: EmployeesIdentifierUninvite,
        PathValues.EMPLOYEES_IDENTIFIER_TERMINATE: EmployeesIdentifierTerminate,
        PathValues.ONBOARDING_WIZARDS: OnboardingWizards,
        PathValues.EMPLOYEES_EMPLOYEE_ID_INVITATIONS: EmployeesEmployeeIdInvitations,
        PathValues.EMPLOYEES_EMPLOYEE_ID_STARTDATE: EmployeesEmployeeIdStartDate,
        PathValues.COMPANY_REPORTS: CompanyReports,
        PathValues.COMPANY_REPORTS_REPORT_ID_DOWNLOAD: CompanyReportsReportIdDownload,
        PathValues.COMPANY_REPORTS_REPORT_ID_DOWNLOADASYNC: CompanyReportsReportIdDownloadAsync,
        PathValues.COMPANY_REPORTS_DOWNLOAD_REPORT_NAME: CompanyReportsDownloadReportName,
        PathValues.PROFILES: Profiles,
        PathValues.AVATARS: Avatars,
        PathValues.AVATARS_EMPLOYEE_ID: AvatarsEmployeeId,
        PathValues.MY_AVATAR: MyAvatar,
        PathValues.TASKS: Tasks,
        PathValues.MY_TASKS: MyTasks,
        PathValues.TASKS_PEOPLE_ID: TasksPeopleId,
        PathValues.TASKS_TASK_ID_COMPLETE: TasksTaskIdComplete,
        PathValues.PEOPLE_ID_EMAIL: PeopleIdEmail,
        PathValues.COMPANY_NAMEDLISTS: CompanyNamedLists,
        PathValues.COMPANY_NAMEDLISTS_LIST_NAME: CompanyNamedListsListName,
        PathValues.COMPANY_NAMEDLISTS_LIST_NAME_ITEM_ID: CompanyNamedListsListNameItemId,
        PathValues.COMPANY_PEOPLE_FIELDS: CompanyPeopleFields,
        PathValues.COMPANY_PEOPLE_FIELDS_FIELD_ID: CompanyPeopleFieldsFieldId,
        PathValues.TIMEOFF_EMPLOYEES_ID_REQUESTS: TimeoffEmployeesIdRequests,
        PathValues.TIMEOFF_EMPLOYEES_ID_DIFF_HOURS_REQUESTS: TimeoffEmployeesIdDiffHoursRequests,
        PathValues.TIMEOFF_EMPLOYEES_ID_REQUESTS_REQUEST_ID: TimeoffEmployeesIdRequestsRequestId,
        PathValues.TIMEOFF_REQUESTS_CHANGES: TimeoffRequestsChanges,
        PathValues.TIMEOFF_WHOSOUT: TimeoffWhosout,
        PathValues.TIMEOFF_OUTTODAY: TimeoffOuttoday,
        PathValues.TIMEOFF_POLICYTYPES_POLICY_TYPE_REASONCODES: TimeoffPolicyTypesPolicyTypeReasonCodes,
        PathValues.TIMEOFF_POLICYTYPES_POLICY_TYPE: TimeoffPolicyTypesPolicyType,
        PathValues.TIMEOFF_POLICYTYPES: TimeoffPolicyTypes,
        PathValues.TIMEOFF_POLICIES: TimeoffPolicies,
        PathValues.TIMEOFF_POLICIES_NAMES: TimeoffPoliciesNames,
        PathValues.TIMEOFF_EMPLOYEES_ID_BALANCE: TimeoffEmployeesIdBalance,
        PathValues.TIMEOFF_EMPLOYEES_ID_ADJUSTMENTS: TimeoffEmployeesIdAdjustments,
        PathValues.ATTENDANCE_IMPORT_IMPORT_METHOD: AttendanceImportImportMethod,
        PathValues.PAYROLL_HISTORY: PayrollHistory,
        PathValues.DOCS_PEOPLE_ID_SHARED: DocsPeopleIdShared,
        PathValues.DOCS_PEOPLE_ID_CONFIDENTIAL: DocsPeopleIdConfidential,
        PathValues.DOCS_PEOPLE_ID_SHARED_UPLOAD: DocsPeopleIdSharedUpload,
        PathValues.DOCS_PEOPLE_ID_CONFIDENTIAL_UPLOAD: DocsPeopleIdConfidentialUpload,
        PathValues.DOCS_PEOPLE_ID_SHARED_DOC_ID: DocsPeopleIdSharedDocId,
        PathValues.DOCS_PEOPLE_ID_CONFIDENTIAL_DOC_ID: DocsPeopleIdConfidentialDocId,
        PathValues.DOCS_PEOPLE_ID: DocsPeopleId,
        PathValues.PEOPLE_ID_WORK: PeopleIdWork,
        PathValues.PEOPLE_ID_WORK_ENTRY_ID: PeopleIdWorkEntryId,
        PathValues.PEOPLE_ID_EMPLOYMENT: PeopleIdEmployment,
        PathValues.PEOPLE_ID_EMPLOYMENT_ENTRY_ID: PeopleIdEmploymentEntryId,
        PathValues.PEOPLE_ID_LIFECYCLE: PeopleIdLifecycle,
        PathValues.PEOPLE_ID_SALARIES: PeopleIdSalaries,
        PathValues.PEOPLE_ID_SALARIES_ENTRY_ID: PeopleIdSalariesEntryId,
        PathValues.PEOPLE_ID_EQUITIES: PeopleIdEquities,
        PathValues.PEOPLE_ID_EQUITIES_ENTRY_ID: PeopleIdEquitiesEntryId,
        PathValues.PEOPLE_ID_VARIABLE: PeopleIdVariable,
        PathValues.PEOPLE_ID_VARIABLE_ENTRY_ID: PeopleIdVariableEntryId,
        PathValues.PEOPLE_ID_TRAINING: PeopleIdTraining,
        PathValues.PEOPLE_ID_TRAINING_ENTRY_ID: PeopleIdTrainingEntryId,
        PathValues.PEOPLE_CUSTOMTABLES_METADATA: PeopleCustomTablesMetadata,
        PathValues.PEOPLE_CUSTOMTABLES_METADATA_CUSTOM_TABLE_ID: PeopleCustomTablesMetadataCustomTableId,
        PathValues.PEOPLE_CUSTOMTABLES_EMPLOYEE_ID_CUSTOM_TABLE_ID: PeopleCustomTablesEmployeeIdCustomTableId,
        PathValues.PEOPLE_CUSTOMTABLES_EMPLOYEE_ID_CUSTOM_TABLE_ID_ENTRY_ID: PeopleCustomTablesEmployeeIdCustomTableIdEntryId,
        PathValues.METADATA_OBJECTS_POSITION: MetadataObjectsPosition,
        PathValues.OBJECTS_POSITION_SEARCH: ObjectsPositionSearch,
    }
)
