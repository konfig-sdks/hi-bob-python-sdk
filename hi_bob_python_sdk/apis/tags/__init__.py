# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from hi_bob_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PEOPLE = "People"
    TABLES = "Tables"
    TIME_OFF = "Time off"
    PAYROLL = "Payroll"
    METADATA = "Metadata"
    DOCUMENTS = "Documents"
    REPORTS = "Reports"
    TASKS = "Tasks"
    CUSTOM_TABLES = "Custom Tables"
    ONBOARDING = "Onboarding"
    ATTENDANCE = "Attendance"
    OBJECTS = "Objects"
