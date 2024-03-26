import typing_extensions

from hi_bob_python_sdk.apis.tags import TagValues
from hi_bob_python_sdk.apis.tags.people_api import PeopleApi
from hi_bob_python_sdk.apis.tags.tables_api import TablesApi
from hi_bob_python_sdk.apis.tags.time_off_api import TimeOffApi
from hi_bob_python_sdk.apis.tags.payroll_api import PayrollApi
from hi_bob_python_sdk.apis.tags.metadata_api import MetadataApi
from hi_bob_python_sdk.apis.tags.documents_api import DocumentsApi
from hi_bob_python_sdk.apis.tags.reports_api import ReportsApi
from hi_bob_python_sdk.apis.tags.tasks_api import TasksApi
from hi_bob_python_sdk.apis.tags.custom_tables_api import CustomTablesApi
from hi_bob_python_sdk.apis.tags.onboarding_api import OnboardingApi
from hi_bob_python_sdk.apis.tags.attendance_api import AttendanceApi
from hi_bob_python_sdk.apis.tags.objects_api import ObjectsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PEOPLE: PeopleApi,
        TagValues.TABLES: TablesApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.METADATA: MetadataApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.TASKS: TasksApi,
        TagValues.CUSTOM_TABLES: CustomTablesApi,
        TagValues.ONBOARDING: OnboardingApi,
        TagValues.ATTENDANCE: AttendanceApi,
        TagValues.OBJECTS: ObjectsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PEOPLE: PeopleApi,
        TagValues.TABLES: TablesApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.METADATA: MetadataApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.TASKS: TasksApi,
        TagValues.CUSTOM_TABLES: CustomTablesApi,
        TagValues.ONBOARDING: OnboardingApi,
        TagValues.ATTENDANCE: AttendanceApi,
        TagValues.OBJECTS: ObjectsApi,
    }
)
