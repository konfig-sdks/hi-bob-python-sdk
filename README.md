<div align="center">

[![Visit Hibob](./header.png)](https://hibob.com)

# Hibob<a id="hibob"></a>

Access your employees data with the Bob API


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`hibob.attendance.import_data`](#hibobattendanceimport_data)
  * [`hibob.custom_tables.create_new_entry`](#hibobcustom_tablescreate_new_entry)
  * [`hibob.custom_tables.delete_entry_by_id`](#hibobcustom_tablesdelete_entry_by_id)
  * [`hibob.custom_tables.read_entries`](#hibobcustom_tablesread_entries)
  * [`hibob.custom_tables.update_entry`](#hibobcustom_tablesupdate_entry)
  * [`hibob.documents.delete_employee_confidential_doc`](#hibobdocumentsdelete_employee_confidential_doc)
  * [`hibob.documents.download_links`](#hibobdocumentsdownload_links)
  * [`hibob.documents.remove_employee_shared_document`](#hibobdocumentsremove_employee_shared_document)
  * [`hibob.documents.upload_confidential_file`](#hibobdocumentsupload_confidential_file)
  * [`hibob.documents.upload_to_confidential_folder`](#hibobdocumentsupload_to_confidential_folder)
  * [`hibob.documents.upload_to_shared_folder`](#hibobdocumentsupload_to_shared_folder)
  * [`hibob.documents.upload_to_shared_folder_0`](#hibobdocumentsupload_to_shared_folder_0)
  * [`hibob.metadata.add_new_field`](#hibobmetadataadd_new_field)
  * [`hibob.metadata.add_new_item_to_named_list`](#hibobmetadataadd_new_item_to_named_list)
  * [`hibob.metadata.delete_field`](#hibobmetadatadelete_field)
  * [`hibob.metadata.delete_item_from_company_named_list`](#hibobmetadatadelete_item_from_company_named_list)
  * [`hibob.metadata.get_company_fields`](#hibobmetadataget_company_fields)
  * [`hibob.metadata.get_company_named_lists`](#hibobmetadataget_company_named_lists)
  * [`hibob.metadata.get_custom_table_metadata`](#hibobmetadataget_custom_table_metadata)
  * [`hibob.metadata.get_named_list`](#hibobmetadataget_named_list)
  * [`hibob.metadata.get_position_fields`](#hibobmetadataget_position_fields)
  * [`hibob.metadata.get_table_details`](#hibobmetadataget_table_details)
  * [`hibob.metadata.update_field`](#hibobmetadataupdate_field)
  * [`hibob.metadata.update_item_from_named_list`](#hibobmetadataupdate_item_from_named_list)
  * [`hibob.objects.search_company_positions`](#hibobobjectssearch_company_positions)
  * [`hibob.onboarding.get_wizard_summary`](#hibobonboardingget_wizard_summary)
  * [`hibob.payroll.create_equity_grant`](#hibobpayrollcreate_equity_grant)
  * [`hibob.payroll.create_new_salary_entry`](#hibobpayrollcreate_new_salary_entry)
  * [`hibob.payroll.create_training_record`](#hibobpayrollcreate_training_record)
  * [`hibob.payroll.create_variable_payment`](#hibobpayrollcreate_variable_payment)
  * [`hibob.payroll.delete_equity_grant`](#hibobpayrolldelete_equity_grant)
  * [`hibob.payroll.delete_salary_entry`](#hibobpayrolldelete_salary_entry)
  * [`hibob.payroll.delete_training_record`](#hibobpayrolldelete_training_record)
  * [`hibob.payroll.delete_training_record_0`](#hibobpayrolldelete_training_record_0)
  * [`hibob.payroll.get_salary_history`](#hibobpayrollget_salary_history)
  * [`hibob.payroll.list_equity_grants`](#hibobpayrolllist_equity_grants)
  * [`hibob.payroll.list_training_records`](#hibobpayrolllist_training_records)
  * [`hibob.payroll.list_variable_payments`](#hibobpayrolllist_variable_payments)
  * [`hibob.payroll.read_history`](#hibobpayrollread_history)
  * [`hibob.payroll.update_equity_grant_for_employee`](#hibobpayrollupdate_equity_grant_for_employee)
  * [`hibob.people.create_employee_record`](#hibobpeoplecreate_employee_record)
  * [`hibob.people.create_employment_entry`](#hibobpeoplecreate_employment_entry)
  * [`hibob.people.create_equity_grant`](#hibobpeoplecreate_equity_grant)
  * [`hibob.people.create_new_salary_entry`](#hibobpeoplecreate_new_salary_entry)
  * [`hibob.people.create_training_record`](#hibobpeoplecreate_training_record)
  * [`hibob.people.create_variable_payment`](#hibobpeoplecreate_variable_payment)
  * [`hibob.people.create_work_entry`](#hibobpeoplecreate_work_entry)
  * [`hibob.people.delete_employment_entry`](#hibobpeopledelete_employment_entry)
  * [`hibob.people.delete_equity_grant`](#hibobpeopledelete_equity_grant)
  * [`hibob.people.delete_salary_entry`](#hibobpeopledelete_salary_entry)
  * [`hibob.people.delete_training_record`](#hibobpeopledelete_training_record)
  * [`hibob.people.delete_training_record_0`](#hibobpeopledelete_training_record_0)
  * [`hibob.people.delete_work_entry`](#hibobpeopledelete_work_entry)
  * [`hibob.people.get_avatar_url`](#hibobpeopleget_avatar_url)
  * [`hibob.people.get_avatar_url_0`](#hibobpeopleget_avatar_url_0)
  * [`hibob.people.get_email_avatar`](#hibobpeopleget_email_avatar)
  * [`hibob.people.get_employment_history`](#hibobpeopleget_employment_history)
  * [`hibob.people.get_salary_history`](#hibobpeopleget_salary_history)
  * [`hibob.people.get_work_history`](#hibobpeopleget_work_history)
  * [`hibob.people.invite_employee_wizard`](#hibobpeopleinvite_employee_wizard)
  * [`hibob.people.list_active_employees`](#hibobpeoplelist_active_employees)
  * [`hibob.people.list_employee_lifecycle`](#hibobpeoplelist_employee_lifecycle)
  * [`hibob.people.list_employees`](#hibobpeoplelist_employees)
  * [`hibob.people.list_equity_grants`](#hibobpeoplelist_equity_grants)
  * [`hibob.people.list_training_records`](#hibobpeoplelist_training_records)
  * [`hibob.people.list_variable_payments`](#hibobpeoplelist_variable_payments)
  * [`hibob.people.read_employee_by_id`](#hibobpeopleread_employee_by_id)
  * [`hibob.people.read_employee_fields`](#hibobpeopleread_employee_fields)
  * [`hibob.people.revoke_access_to_employee`](#hibobpeoplerevoke_access_to_employee)
  * [`hibob.people.search_employees`](#hibobpeoplesearch_employees)
  * [`hibob.people.set_start_date`](#hibobpeopleset_start_date)
  * [`hibob.people.terminate_employee`](#hibobpeopleterminate_employee)
  * [`hibob.people.update_email`](#hibobpeopleupdate_email)
  * [`hibob.people.update_employee_record`](#hibobpeopleupdate_employee_record)
  * [`hibob.people.update_employment_entry`](#hibobpeopleupdate_employment_entry)
  * [`hibob.people.update_equity_grant_for_employee`](#hibobpeopleupdate_equity_grant_for_employee)
  * [`hibob.people.update_work_entry`](#hibobpeopleupdate_work_entry)
  * [`hibob.people.upload_employee_avatar_url`](#hibobpeopleupload_employee_avatar_url)
  * [`hibob.reports.download_by_id`](#hibobreportsdownload_by_id)
  * [`hibob.reports.download_report_file`](#hibobreportsdownload_report_file)
  * [`hibob.reports.get_download_url`](#hibobreportsget_download_url)
  * [`hibob.reports.list_accessible_reports`](#hibobreportslist_accessible_reports)
  * [`hibob.tables.create_employment_entry`](#hibobtablescreate_employment_entry)
  * [`hibob.tables.create_equity_grant`](#hibobtablescreate_equity_grant)
  * [`hibob.tables.create_new_salary_entry`](#hibobtablescreate_new_salary_entry)
  * [`hibob.tables.create_training_record`](#hibobtablescreate_training_record)
  * [`hibob.tables.create_variable_payment`](#hibobtablescreate_variable_payment)
  * [`hibob.tables.create_work_entry`](#hibobtablescreate_work_entry)
  * [`hibob.tables.delete_employment_entry`](#hibobtablesdelete_employment_entry)
  * [`hibob.tables.delete_equity_grant`](#hibobtablesdelete_equity_grant)
  * [`hibob.tables.delete_salary_entry`](#hibobtablesdelete_salary_entry)
  * [`hibob.tables.delete_training_record`](#hibobtablesdelete_training_record)
  * [`hibob.tables.delete_training_record_0`](#hibobtablesdelete_training_record_0)
  * [`hibob.tables.delete_work_entry`](#hibobtablesdelete_work_entry)
  * [`hibob.tables.get_employment_history`](#hibobtablesget_employment_history)
  * [`hibob.tables.get_salary_history`](#hibobtablesget_salary_history)
  * [`hibob.tables.get_work_history`](#hibobtablesget_work_history)
  * [`hibob.tables.list_employee_lifecycle`](#hibobtableslist_employee_lifecycle)
  * [`hibob.tables.list_equity_grants`](#hibobtableslist_equity_grants)
  * [`hibob.tables.list_training_records`](#hibobtableslist_training_records)
  * [`hibob.tables.list_variable_payments`](#hibobtableslist_variable_payments)
  * [`hibob.tables.update_employment_entry`](#hibobtablesupdate_employment_entry)
  * [`hibob.tables.update_equity_grant_for_employee`](#hibobtablesupdate_equity_grant_for_employee)
  * [`hibob.tables.update_work_entry`](#hibobtablesupdate_work_entry)
  * [`hibob.tasks.complete_task`](#hibobtaskscomplete_task)
  * [`hibob.tasks.get_employee_tasks`](#hibobtasksget_employee_tasks)
  * [`hibob.tasks.get_open_tasks`](#hibobtasksget_open_tasks)
  * [`hibob.tasks.read_employee_tasks`](#hibobtasksread_employee_tasks)
  * [`hibob.time_off.add_reason_codes`](#hibobtime_offadd_reason_codes)
  * [`hibob.time_off.cancel_request`](#hibobtime_offcancel_request)
  * [`hibob.time_off.create_balance_adjustment`](#hibobtime_offcreate_balance_adjustment)
  * [`hibob.time_off.get_details_of_request`](#hibobtime_offget_details_of_request)
  * [`hibob.time_off.get_employee_balance`](#hibobtime_offget_employee_balance)
  * [`hibob.time_off.get_new_deleted_requests_since_date`](#hibobtime_offget_new_deleted_requests_since_date)
  * [`hibob.time_off.get_out_of_office`](#hibobtime_offget_out_of_office)
  * [`hibob.time_off.get_policy_details`](#hibobtime_offget_policy_details)
  * [`hibob.time_off.get_policy_details_0`](#hibobtime_offget_policy_details_0)
  * [`hibob.time_off.get_whos_out`](#hibobtime_offget_whos_out)
  * [`hibob.time_off.list_policy_type_names`](#hibobtime_offlist_policy_type_names)
  * [`hibob.time_off.list_policy_types_names`](#hibobtime_offlist_policy_types_names)
  * [`hibob.time_off.list_reason_codes`](#hibobtime_offlist_reason_codes)
  * [`hibob.time_off.submit_new_request`](#hibobtime_offsubmit_new_request)
  * [`hibob.time_off.submit_new_request_diff_hours`](#hibobtime_offsubmit_new_request_diff_hours)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=HiBob&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from hi_bob_python_sdk import HiBob, ApiException

hibob = HiBob(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

try:
    # Import attendance data
    import_data_response = hibob.attendance.import_data(
        id_type="string_example",
        requests=[
        {
            "id": "12356733644",
            "clock_in": "2022-06-12T08:00",
            "clock_out": "2022-06-12T17:00",
        }
    ],
        import_method="aggregate",
        date_time_format="yyyy-MM-dd hh:mm a",
    )
    print(import_data_response)
except ApiException as e:
    print("Exception when calling AttendanceApi.import_data: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from hi_bob_python_sdk import HiBob, ApiException

hibob = HiBob(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

async def main():
    try:
        # Import attendance data
        import_data_response = await hibob.attendance.aimport_data(
            id_type="string_example",
            requests=[
        {
            "id": "12356733644",
            "clock_in": "2022-06-12T08:00",
            "clock_out": "2022-06-12T17:00",
        }
    ],
            import_method="aggregate",
            date_time_format="yyyy-MM-dd hh:mm a",
        )
        print(import_data_response)
    except ApiException as e:
        print("Exception when calling AttendanceApi.import_data: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from hi_bob_python_sdk import HiBob, ApiException

hibob = HiBob(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

try:
    # Import attendance data
    import_data_response = hibob.attendance.raw.import_data(
        id_type="string_example",
        requests=[
        {
            "id": "12356733644",
            "clock_in": "2022-06-12T08:00",
            "clock_out": "2022-06-12T17:00",
        }
    ],
        import_method="aggregate",
        date_time_format="yyyy-MM-dd hh:mm a",
    )
    pprint(import_data_response.body)
    pprint(import_data_response.body["status"])
    pprint(import_data_response.body["total"])
    pprint(import_data_response.body["imported"])
    pprint(import_data_response.body["not_imported"])
    pprint(import_data_response.body["errors"])
    pprint(import_data_response.headers)
    pprint(import_data_response.status)
    pprint(import_data_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AttendanceApi.import_data: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `hibob.attendance.import_data`<a id="hibobattendanceimport_data"></a>

Import attendance data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_data_response = hibob.attendance.import_data(
    id_type="string_example",
    requests=[
        {
            "id": "12356733644",
            "clock_in": "2022-06-12T08:00",
            "clock_out": "2022-06-12T17:00",
        }
    ],
    import_method="aggregate",
    date_time_format="yyyy-MM-dd hh:mm a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_type: `str`<a id="id_type-str"></a>

The ID type used to identify the employee. Can be one of: \\\"bobId\\\", \\\"email\\\", \\\"idInCompany\\\", or a custom field.<br/>For <b>custom fields</b> a forward slash separator should be used.<br/>In order to use a specific custom field to identify an employee, for example a custom field called \\\"Payroll integration ID\\\":<ul><li>Query the field name via the <a href='https://apidocs.hibob.com/reference/get_company-people-fields'>\\\"Get all company fields\\\"</a></li><li>In the response the name will look like <b>\\\"identification.custom.Payroll Integration ID_1RNhIIf\\\"</b></li><li>The value to use should be: <b>\\\"/identification/custom/Payroll Integration ID_1RNhI\\\"</b></li></ul>

##### requests: List[`ImportAttendanceEvent`]<a id="requests-listimportattendanceevent"></a>

List of attendance events

##### import_method: `str`<a id="import_method-str"></a>

Indicates if the provided data should be processed via an aggregation engine or immediately. <ul>Aggregate - will add the logs to a temporary location, and an aggregation job will process the data asynchronously.</ul><ul>Immediate - will insert the records as-is.</ul>

##### date_time_format: `str`<a id="date_time_format-str"></a>

Allows to set custom date format for the date-time values sent in the requests

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImportAttendanceData`](./hi_bob_python_sdk/type/import_attendance_data.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImportAttendanceResponse`](./hi_bob_python_sdk/pydantic/import_attendance_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/import/{importMethod}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.custom_tables.create_new_entry`<a id="hibobcustom_tablescreate_new_entry"></a>

Create new custom table entry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.custom_tables.create_new_entry(
    employee_id="employee_id_example",
    custom_table_id="custom_table_id_example",
    raw_body="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Employee ID.

##### custom_table_id: `str`<a id="custom_table_id-str"></a>

The ID of custom table.

##### raw_body: `str`<a id="raw_body-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomTablesCreateNewEntryRequest`](./hi_bob_python_sdk/type/custom_tables_create_new_entry_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/custom-tables/{employee_id}/{custom_table_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.custom_tables.delete_entry_by_id`<a id="hibobcustom_tablesdelete_entry_by_id"></a>

Delete custom table entry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.custom_tables.delete_entry_by_id(
    employee_id="employee_id_example",
    custom_table_id="custom_table_id_example",
    entry_id="entry_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Employee ID.

##### custom_table_id: `str`<a id="custom_table_id-str"></a>

The ID of custom table.

##### entry_id: `str`<a id="entry_id-str"></a>

The ID of custom table entry.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/custom-tables/{employee_id}/{custom_table_id}/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.custom_tables.read_entries`<a id="hibobcustom_tablesread_entries"></a>

Read all entries of the given custom table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
read_entries_response = hibob.custom_tables.read_entries(
    employee_id="employee_id_example",
    custom_table_id="custom_table_id_example",
    include_human_readable=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Employee ID.

##### custom_table_id: `str`<a id="custom_table_id-str"></a>

The ID of custom table.

##### include_human_readable: `bool`<a id="include_human_readable-bool"></a>

Whether to include the additional \"humanReadable\" JSON node in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomTableEntriesList`](./hi_bob_python_sdk/pydantic/custom_table_entries_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/custom-tables/{employee_id}/{custom_table_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.custom_tables.update_entry`<a id="hibobcustom_tablesupdate_entry"></a>

Update custom table entry

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.custom_tables.update_entry(
    employee_id="employee_id_example",
    custom_table_id="custom_table_id_example",
    entry_id="entry_id_example",
    raw_body="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Employee ID.

##### custom_table_id: `str`<a id="custom_table_id-str"></a>

The ID of custom table.

##### entry_id: `str`<a id="entry_id-str"></a>

The ID of custom table entry.

##### raw_body: `str`<a id="raw_body-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomTablesUpdateEntryRequest`](./hi_bob_python_sdk/type/custom_tables_update_entry_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/custom-tables/{employee_id}/{custom_table_id}/{entry_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.documents.delete_employee_confidential_doc`<a id="hibobdocumentsdelete_employee_confidential_doc"></a>

Delete a specific document from the employee's confidential folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.documents.delete_employee_confidential_doc(
    id="id_example",
    doc_id="docId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### doc_id: `str`<a id="doc_id-str"></a>

Document ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/docs/people/{id}/confidential/{docId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.documents.download_links`<a id="hibobdocumentsdownload_links"></a>

Returns a list of documents and download links.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_links_response = hibob.documents.download_links(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeDocumentResponse`](./hi_bob_python_sdk/pydantic/employee_document_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/docs/people/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.documents.remove_employee_shared_document`<a id="hibobdocumentsremove_employee_shared_document"></a>

Delete specific document from the employee's shared folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.documents.remove_employee_shared_document(
    id="id_example",
    doc_id="docId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### doc_id: `str`<a id="doc_id-str"></a>

Document ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/docs/people/{id}/shared/{docId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.documents.upload_confidential_file`<a id="hibobdocumentsupload_confidential_file"></a>

Upload a file to the employee's confidential folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.documents.upload_confidential_file(
    body=None,
    id="id_example",
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

employee id

##### file: `IO`<a id="file-io"></a>

The file to upload.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentsUploadConfidentialFileRequest`](./hi_bob_python_sdk/type/documents_upload_confidential_file_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/docs/people/{id}/confidential/upload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.documents.upload_to_confidential_folder`<a id="hibobdocumentsupload_to_confidential_folder"></a>

Upload a document to the employee's confidential folder

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.documents.upload_to_confidential_folder(
    id="id_example",
    tags=[
        "string_example"
    ],
    document_name="string_example",
    document_url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### tags: [`AddDocumentTags`](./hi_bob_python_sdk/type/add_document_tags.py)<a id="tags-adddocumenttagshi_bob_python_sdktypeadd_document_tagspy"></a>

##### document_name: `str`<a id="document_name-str"></a>

Document name.

##### document_url: `str`<a id="document_url-str"></a>

URL of the document to upload.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddDocument`](./hi_bob_python_sdk/type/add_document.py)
Document to upload.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/docs/people/{id}/confidential` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.documents.upload_to_shared_folder`<a id="hibobdocumentsupload_to_shared_folder"></a>

Upload a document to the employee's shared folder

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.documents.upload_to_shared_folder(
    id="id_example",
    tags=[
        "string_example"
    ],
    document_name="string_example",
    document_url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### tags: [`AddDocumentTags`](./hi_bob_python_sdk/type/add_document_tags.py)<a id="tags-adddocumenttagshi_bob_python_sdktypeadd_document_tagspy"></a>

##### document_name: `str`<a id="document_name-str"></a>

Document name.

##### document_url: `str`<a id="document_url-str"></a>

URL of the document to upload.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddDocument`](./hi_bob_python_sdk/type/add_document.py)
Document to upload.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/docs/people/{id}/shared` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.documents.upload_to_shared_folder_0`<a id="hibobdocumentsupload_to_shared_folder_0"></a>

Upload a file to the employee's shared folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.documents.upload_to_shared_folder_0(
    body=None,
    id="id_example",
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### file: `IO`<a id="file-io"></a>

The file to upload.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentsUploadToSharedFolderRequest`](./hi_bob_python_sdk/type/documents_upload_to_shared_folder_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/docs/people/{id}/shared/upload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.add_new_field`<a id="hibobmetadataadd_new_field"></a>

Create a new field.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_field_response = hibob.metadata.add_new_field(
    name="string_example",
    category="string_example",
    type="string_example",
    description="string_example",
    historical="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the field.

##### category: `str`<a id="category-str"></a>

The category of the field.

##### type: `str`<a id="type-str"></a>

The type of field. Supported field types: text, text-area, number, date, list, multi-list, hierarchy-list, currency, employee-reference, document.

##### description: `str`<a id="description-str"></a>

The description of the field.

##### historical: `str`<a id="historical-str"></a>

When true, this field keeps the history of its values, each being active starting from a certain date. The default value is false.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateFieldRequest`](./hi_bob_python_sdk/type/create_field_request.py)
The field to be created.

#### 🔄 Return<a id="🔄-return"></a>

[`FieldId`](./hi_bob_python_sdk/pydantic/field_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/people/fields` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.add_new_item_to_named_list`<a id="hibobmetadataadd_new_item_to_named_list"></a>

Add a new item to an existing list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_item_to_named_list_response = hibob.metadata.add_new_item_to_named_list(
    name="string_example",
    list_name="listName_example",
    parent_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the item.

##### list_name: `str`<a id="list_name-str"></a>

The internal name of the list.

##### parent_id: `int`<a id="parent_id-int"></a>

ID of the new hierarchy parent node.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewListItem`](./hi_bob_python_sdk/type/new_list_item.py)
The <b>parentId</b> attribute is optional and only applies to hierarchy lists. When <b>parentId</b> is specified, the newly created list item will be placed under the specific hierarchy parent node.

#### 🔄 Return<a id="🔄-return"></a>

[`FlatListItemId`](./hi_bob_python_sdk/pydantic/flat_list_item_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/named-lists/{listName}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.delete_field`<a id="hibobmetadatadelete_field"></a>

Delete an existing field.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.metadata.delete_field(
    field_id="fieldId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_id: `str`<a id="field_id-str"></a>

The ID of the field.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/people/fields/{fieldId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.delete_item_from_company_named_list`<a id="hibobmetadatadelete_item_from_company_named_list"></a>

Delete an item from an existing list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.metadata.delete_item_from_company_named_list(
    list_name="listName_example",
    item_id="itemId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_name: `str`<a id="list_name-str"></a>

The internal name of the list.

##### item_id: `str`<a id="item_id-str"></a>

The ID of the list item.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/named-lists/{listName}/{itemId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.get_company_fields`<a id="hibobmetadataget_company_fields"></a>

Get all company fields.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_fields_response = hibob.metadata.get_company_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Fields`](./hi_bob_python_sdk/pydantic/fields.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/people/fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.get_company_named_lists`<a id="hibobmetadataget_company_named_lists"></a>

Get all company lists

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_named_lists_response = hibob.metadata.get_company_named_lists(
    include_archived=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### include_archived: `bool`<a id="include_archived-bool"></a>

Whether to include archived items in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`Lists`](./hi_bob_python_sdk/pydantic/lists.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/named-lists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.get_custom_table_metadata`<a id="hibobmetadataget_custom_table_metadata"></a>

Read metadata of custom tables defined

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_table_metadata_response = hibob.metadata.get_custom_table_metadata()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomTableMetadataList`](./hi_bob_python_sdk/pydantic/custom_table_metadata_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/custom-tables/metadata` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.get_named_list`<a id="hibobmetadataget_named_list"></a>

Get a specific company list by name.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_named_list_response = hibob.metadata.get_named_list(
    list_name="listName_example",
    include_archived=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_name: `str`<a id="list_name-str"></a>

The internal name of the list.

##### include_archived: `bool`<a id="include_archived-bool"></a>

Whether to include archived items in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`ModelList`](./hi_bob_python_sdk/pydantic/model_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/named-lists/{listName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.get_position_fields`<a id="hibobmetadataget_position_fields"></a>

Returns a list of all fields of object type position.<br/>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_position_fields_response = hibob.metadata.get_position_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ObjectsMetadata`](./hi_bob_python_sdk/pydantic/objects_metadata.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata/objects/position` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.get_table_details`<a id="hibobmetadataget_table_details"></a>

Read metadata for specific custom table

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_table_details_response = hibob.metadata.get_table_details(
    custom_table_id="custom_table_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_table_id: `str`<a id="custom_table_id-str"></a>

The ID of custom table.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomTableMetadata`](./hi_bob_python_sdk/pydantic/custom_table_metadata.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/custom-tables/metadata/{custom_table_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.update_field`<a id="hibobmetadataupdate_field"></a>

Update an existing field

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.metadata.update_field(
    field_id="fieldId_example",
    description="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_id: `str`<a id="field_id-str"></a>

The ID of the field.

##### description: `str`<a id="description-str"></a>

The description of the field.

##### name: `str`<a id="name-str"></a>

The name of the field.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateFieldRequest`](./hi_bob_python_sdk/type/update_field_request.py)
The new name and/or description of the updated field.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/people/fields/{fieldId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.metadata.update_item_from_named_list`<a id="hibobmetadataupdate_item_from_named_list"></a>

Update an existing item from a list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.metadata.update_item_from_named_list(
    list_name="listName_example",
    item_id="itemId_example",
    name="string_example",
    parent_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_name: `str`<a id="list_name-str"></a>

The internal name of the list.

##### item_id: `str`<a id="item_id-str"></a>

The ID of the list item.

##### name: `str`<a id="name-str"></a>

Name of the item.

##### parent_id: `int`<a id="parent_id-int"></a>

ID of the new hierarchy parent node.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateListItemRequest`](./hi_bob_python_sdk/type/update_list_item_request.py)
You need to provide at least one of: <b>name</b> or <b>parentId</b>. Providing a name will rename the list item value. Providing the parent ID will move the hierarchy list item (together with its children) under the indicated parent node.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/named-lists/{listName}/{itemId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.objects.search_company_positions`<a id="hibobobjectssearch_company_positions"></a>

Returns a list of the company positions, filtered by the specified attributes.  <br /><br><b>Note</b>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_company_positions_response = hibob.objects.search_company_positions(
    fields=[
        "string_example"
    ],
    filters=[
        None
    ],
    include_human_readable=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: [`GetPositionsRequestFields`](./hi_bob_python_sdk/type/get_positions_request_fields.py)<a id="fields-getpositionsrequestfieldshi_bob_python_sdktypeget_positions_request_fieldspy"></a>

##### filters: List[`FilterInstruction`]<a id="filters-listfilterinstruction"></a>

##### include_human_readable: `bool`<a id="include_human_readable-bool"></a>

Whether to include the additional \\\"humanReadable\\\" entry in the response.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetPositionsRequest`](./hi_bob_python_sdk/type/get_positions_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PositionEntries`](./hi_bob_python_sdk/pydantic/position_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/objects/position/search` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.onboarding.get_wizard_summary`<a id="hibobonboardingget_wizard_summary"></a>

Wizard info includes Wizard ID, name and description.<br /><b>Supported user types:</b> Service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_wizard_summary_response = hibob.onboarding.get_wizard_summary()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OnboardingWizards`](./hi_bob_python_sdk/pydantic/onboarding_wizards.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/onboarding/wizards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.create_equity_grant`<a id="hibobpayrollcreate_equity_grant"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.payroll.create_equity_grant(
    body=None,
    quantity=3.14,
    equity_type="string_example",
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    vesting_commencement_date="1970-01-01",
    consent_number="string_example",
    grant_date="1970-01-01",
    option_expiration="1970-01-01",
    exercise_price={
        "value": 3.14,
        "currency": "currency_example",
    },
    vesting_term="string_example",
    grant_type="string_example",
    vesting_schedule=3.14,
    grant_number=3.14,
    grant_status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`EquityEntry`](./hi_bob_python_sdk/type/equity_entry.py)<a id="requestbody-equityentryhi_bob_python_sdktypeequity_entrypy"></a>

Equity grant to add.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.create_new_salary_entry`<a id="hibobpayrollcreate_new_salary_entry"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.payroll.create_new_salary_entry(
    body=None,
    base={
        "value": 3.14,
        "currency": "currency_example",
    },
    pay_period="string_example",
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    pay_frequency="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`SalaryEntry`](./hi_bob_python_sdk/type/salary_entry.py)<a id="requestbody-salaryentryhi_bob_python_sdktypesalary_entrypy"></a>

Salary entry to add. This must not conflict with another entry on the same effective date.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/salaries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.create_training_record`<a id="hibobpayrollcreate_training_record"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.payroll.create_training_record(
    body=None,
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    description="string_example",
    name="string_example",
    cost={
        "value": 3.14,
        "currency": "currency_example",
    },
    status="string_example",
    frequency="string_example",
    start_date="1970-01-01",
    end_date="1970-01-01",
    document_id=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`TrainingEntry`](./hi_bob_python_sdk/type/training_entry.py)<a id="requestbody-trainingentryhi_bob_python_sdktypetraining_entrypy"></a>

Training entry to add.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/training` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.create_variable_payment`<a id="hibobpayrollcreate_variable_payment"></a>

<br><br><b>Note</b>:The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.payroll.create_variable_payment(
    body=None,
    amount={
        "value": 3.14,
        "currency": "currency_example",
    },
    payment_period="string_example",
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    variable_type="string_example",
    company_percent=3.14,
    department_percent=3.14,
    individual_percent=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`VariableEntry`](./hi_bob_python_sdk/type/variable_entry.py)<a id="requestbody-variableentryhi_bob_python_sdktypevariable_entrypy"></a>

Variable payment to add.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/variable` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.delete_equity_grant`<a id="hibobpayrolldelete_equity_grant"></a>

Deletes an equity grant for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.payroll.delete_equity_grant(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The Entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.delete_salary_entry`<a id="hibobpayrolldelete_salary_entry"></a>

Deletes a salary entry from the employee's list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.payroll.delete_salary_entry(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/salaries/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.delete_training_record`<a id="hibobpayrolldelete_training_record"></a>

Deletes a training record for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.payroll.delete_training_record(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The Entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/variable/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.delete_training_record_0`<a id="hibobpayrolldelete_training_record_0"></a>

Deletes any training records for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.payroll.delete_training_record_0(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The Entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/training/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.get_salary_history`<a id="hibobpayrollget_salary_history"></a>

Returns a list of salary history entries for a given employee.<br /><br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_salary_history_response = hibob.payroll.get_salary_history(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`SalaryEntries`](./hi_bob_python_sdk/pydantic/salary_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/salaries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.list_equity_grants`<a id="hibobpayrolllist_equity_grants"></a>

Returns a list of equity grants for a given employee.<br /><b>Supported user types:</b> Service<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_equity_grants_response = hibob.payroll.list_equity_grants(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`EquityEntries`](./hi_bob_python_sdk/pydantic/equity_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.list_training_records`<a id="hibobpayrolllist_training_records"></a>

Returns a list of training records for a given employee<br /><br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_training_records_response = hibob.payroll.list_training_records(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingEntries`](./hi_bob_python_sdk/pydantic/training_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/training` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.list_variable_payments`<a id="hibobpayrolllist_variable_payments"></a>

Returns a list of variable payments for a given employee.<br /><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_variable_payments_response = hibob.payroll.list_variable_payments(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`VariableEntries`](./hi_bob_python_sdk/pydantic/variable_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/variable` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.read_history`<a id="hibobpayrollread_history"></a>

Read payroll history.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
read_history_response = hibob.payroll.read_history(
    department="string_example",
    show_inactive=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department: `str`<a id="department-str"></a>

filter payroll for specific department.

##### show_inactive: `bool`<a id="show_inactive-bool"></a>

Whether to include inactive employees in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`Employees`](./hi_bob_python_sdk/pydantic/employees.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.payroll.update_equity_grant_for_employee`<a id="hibobpayrollupdate_equity_grant_for_employee"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>. - Basic: [] - Bearer: []

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.payroll.update_equity_grant_for_employee(
    body=None,
    quantity=3.14,
    equity_type="string_example",
    id="id_example",
    entry_id=1,
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    vesting_commencement_date="1970-01-01",
    consent_number="string_example",
    grant_date="1970-01-01",
    option_expiration="1970-01-01",
    exercise_price={
        "value": 3.14,
        "currency": "currency_example",
    },
    vesting_term="string_example",
    grant_type="string_example",
    vesting_schedule=3.14,
    grant_number=3.14,
    grant_status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to update.

##### requestBody: [`EquityEntry`](./hi_bob_python_sdk/type/equity_entry.py)<a id="requestbody-equityentryhi_bob_python_sdktypeequity_entrypy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities/{entry_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.create_employee_record`<a id="hibobpeoplecreate_employee_record"></a>

<b>Note:</b> Changes to this API are planned to take effect on May 31, 2024.  Make sure to review all of the details in the <a href='https://help.hibob.com/hc/en-us/articles/19726260483601'>Working pattern API Changes</a>  article in the help center.<br> <br>This creates a new employee record in Bob. You can include only the fields listed in the  [Fields Metadata API](https://apidocs.hibob.com/reference/get_company-people-fields).  <br /><br><b>Note</b>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_employee_record_response = hibob.people.create_employee_record(
    first_name="string_example",
    surname="string_example",
    email="string_example",
    work={
        "site": "site_example",
        "start_date": "1970-01-01",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

Employee's first name.

##### surname: `str`<a id="surname-str"></a>

Employee's surname.

##### email: `str`<a id="email-str"></a>

Employee's email address.

##### work: [`CreateEmployeeRequestWork`](./hi_bob_python_sdk/type/create_employee_request_work.py)<a id="work-createemployeerequestworkhi_bob_python_sdktypecreate_employee_request_workpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEmployeeRequest`](./hi_bob_python_sdk/type/create_employee_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./hi_bob_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.create_employment_entry`<a id="hibobpeoplecreate_employment_entry"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.create_employment_entry(
    body=None,
    effective_date="1970-01-01",
    id="id_example",
    id=1,
    reason="string_example",
    contract="string_example",
    type="string_example",
    salary_pay_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

employee id

##### requestBody: [`EmploymentEntry`](./hi_bob_python_sdk/type/employment_entry.py)<a id="requestbody-employmententryhi_bob_python_sdktypeemployment_entrypy"></a>

Employment entry to add. This must not conflict with another entry on the same effective date.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/employment` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.create_equity_grant`<a id="hibobpeoplecreate_equity_grant"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.create_equity_grant(
    body=None,
    quantity=3.14,
    equity_type="string_example",
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    vesting_commencement_date="1970-01-01",
    consent_number="string_example",
    grant_date="1970-01-01",
    option_expiration="1970-01-01",
    exercise_price={
        "value": 3.14,
        "currency": "currency_example",
    },
    vesting_term="string_example",
    grant_type="string_example",
    vesting_schedule=3.14,
    grant_number=3.14,
    grant_status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`EquityEntry`](./hi_bob_python_sdk/type/equity_entry.py)<a id="requestbody-equityentryhi_bob_python_sdktypeequity_entrypy"></a>

Equity grant to add.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.create_new_salary_entry`<a id="hibobpeoplecreate_new_salary_entry"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.create_new_salary_entry(
    body=None,
    base={
        "value": 3.14,
        "currency": "currency_example",
    },
    pay_period="string_example",
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    pay_frequency="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`SalaryEntry`](./hi_bob_python_sdk/type/salary_entry.py)<a id="requestbody-salaryentryhi_bob_python_sdktypesalary_entrypy"></a>

Salary entry to add. This must not conflict with another entry on the same effective date.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/salaries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.create_training_record`<a id="hibobpeoplecreate_training_record"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.create_training_record(
    body=None,
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    description="string_example",
    name="string_example",
    cost={
        "value": 3.14,
        "currency": "currency_example",
    },
    status="string_example",
    frequency="string_example",
    start_date="1970-01-01",
    end_date="1970-01-01",
    document_id=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`TrainingEntry`](./hi_bob_python_sdk/type/training_entry.py)<a id="requestbody-trainingentryhi_bob_python_sdktypetraining_entrypy"></a>

Training entry to add.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/training` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.create_variable_payment`<a id="hibobpeoplecreate_variable_payment"></a>

<br><br><b>Note</b>:The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.create_variable_payment(
    body=None,
    amount={
        "value": 3.14,
        "currency": "currency_example",
    },
    payment_period="string_example",
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    variable_type="string_example",
    company_percent=3.14,
    department_percent=3.14,
    individual_percent=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`VariableEntry`](./hi_bob_python_sdk/type/variable_entry.py)<a id="requestbody-variableentryhi_bob_python_sdktypevariable_entrypy"></a>

Variable payment to add.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/variable` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.create_work_entry`<a id="hibobpeoplecreate_work_entry"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.create_work_entry(
    body=None,
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    title="string_example",
    department="string_example",
    site="string_example",
    site_id=1,
    reports_to={
        "id": "id_example",
    },
    custom_columns={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`WorkEntry`](./hi_bob_python_sdk/type/work_entry.py)<a id="requestbody-workentryhi_bob_python_sdktypework_entrypy"></a>

Work entry to add. This must not conflict with another entry on the same effective date.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/work` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.delete_employment_entry`<a id="hibobpeopledelete_employment_entry"></a>

Deletes an employment entry from a given employee's employment history.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.delete_employment_entry(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/employment/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.delete_equity_grant`<a id="hibobpeopledelete_equity_grant"></a>

Deletes an equity grant for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.delete_equity_grant(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The Entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.delete_salary_entry`<a id="hibobpeopledelete_salary_entry"></a>

Deletes a salary entry from the employee's list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.delete_salary_entry(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/salaries/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.delete_training_record`<a id="hibobpeopledelete_training_record"></a>

Deletes a training record for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.delete_training_record(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The Entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/variable/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.delete_training_record_0`<a id="hibobpeopledelete_training_record_0"></a>

Deletes any training records for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.delete_training_record_0(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The Entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/training/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.delete_work_entry`<a id="hibobpeopledelete_work_entry"></a>

Deletes a work entry from a given employee's work history.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.delete_work_entry(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/work/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.get_avatar_url`<a id="hibobpeopleget_avatar_url"></a>

Returns the avatar image URL of the employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.get_avatar_url(
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

employee id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.get_avatar_url_0`<a id="hibobpeopleget_avatar_url_0"></a>

Returns the avatar image URL of the logged-in user.<b>Supported user types:</b> Employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.get_avatar_url_0()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/my/avatar` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.get_email_avatar`<a id="hibobpeopleget_email_avatar"></a>

Returns the avatar image URL of the employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.get_email_avatar(
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Employee email.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.get_employment_history`<a id="hibobpeopleget_employment_history"></a>

<b>Note:</b> Changes to this API are planned to take effect on May 31, 2024.  Make sure to review all of the details in the <a href='https://help.hibob.com/hc/en-us/articles/19726260483601'>Working pattern API Changes</a>  article in the help center.<br> <br>Returns a list of employment history entries for a given employee.<br /><br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employment_history_response = hibob.people.get_employment_history(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

employee id

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentEntries`](./hi_bob_python_sdk/pydantic/employment_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/employment` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.get_salary_history`<a id="hibobpeopleget_salary_history"></a>

Returns a list of salary history entries for a given employee.<br /><br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_salary_history_response = hibob.people.get_salary_history(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`SalaryEntries`](./hi_bob_python_sdk/pydantic/salary_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/salaries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.get_work_history`<a id="hibobpeopleget_work_history"></a>

Returns a list of work history entries for a given employee.<br /><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_history_response = hibob.people.get_work_history(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkEntries`](./hi_bob_python_sdk/pydantic/work_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/work` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.invite_employee_wizard`<a id="hibobpeopleinvite_employee_wizard"></a>

Invite an employee with a welcome wizard ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.invite_employee_wizard(
    welcome_wizard_id=1,
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### welcome_wizard_id: `int`<a id="welcome_wizard_id-int"></a>

The Welcome wizard ID.

##### employee_id: `str`<a id="employee_id-str"></a>

Employee ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InvitationByWizard`](./hi_bob_python_sdk/type/invitation_by_wizard.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/invitations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.list_active_employees`<a id="hibobpeoplelist_active_employees"></a>

Returns the public section of all  active employees of the logged-in user company.<br /><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value. Use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_active_employees_response = hibob.people.list_active_employees(
    sort_by="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort_by: `str`<a id="sort_by-str"></a>

Optional field name to sort by. This defaults to firstName.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesProfiles`](./hi_bob_python_sdk/pydantic/employees_profiles.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.list_employee_lifecycle`<a id="hibobpeoplelist_employee_lifecycle"></a>

Returns a list of life-cycle history entries for a given employee.<br /><br><br><b>Note</b>: TThe values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employee_lifecycle_response = hibob.people.list_employee_lifecycle(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`LifeCycleEntries`](./hi_bob_python_sdk/pydantic/life_cycle_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/lifecycle` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.list_employees`<a id="hibobpeoplelist_employees"></a>

<b>Note:</b> Deprecated at the end of March 2024. Please use <b>/people/search</b> ("Search for employees") instead. <br/><br/> This returns a list of all active employees. The data is filtered based on the access level of the logged-in user. Only viewable categories are returned.<br /><br> <b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employees_response = hibob.people.list_employees(
    show_inactive=True,
    human_readable=False,
    include_human_readable=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### show_inactive: `bool`<a id="show_inactive-bool"></a>

Should include inactive employees.

##### human_readable: `bool`<a id="human_readable-bool"></a>

Whether to supply humanReadable values in JSON instead of machine-readable format (default).

##### include_human_readable: `bool`<a id="include_human_readable-bool"></a>

Whether to include the additional \"humanReadable\" JSON node in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`Employees`](./hi_bob_python_sdk/pydantic/employees.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.list_equity_grants`<a id="hibobpeoplelist_equity_grants"></a>

Returns a list of equity grants for a given employee.<br /><b>Supported user types:</b> Service<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_equity_grants_response = hibob.people.list_equity_grants(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`EquityEntries`](./hi_bob_python_sdk/pydantic/equity_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.list_training_records`<a id="hibobpeoplelist_training_records"></a>

Returns a list of training records for a given employee<br /><br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_training_records_response = hibob.people.list_training_records(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingEntries`](./hi_bob_python_sdk/pydantic/training_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/training` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.list_variable_payments`<a id="hibobpeoplelist_variable_payments"></a>

Returns a list of variable payments for a given employee.<br /><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_variable_payments_response = hibob.people.list_variable_payments(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`VariableEntries`](./hi_bob_python_sdk/pydantic/variable_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/variable` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.read_employee_by_id`<a id="hibobpeopleread_employee_by_id"></a>

<b>Note:</b> Deprecated at the end of March 2024. Please use <b>POST /people/{identifier}</b> ("Read company employee fields by ID.") instead. <br/><br/> Returns the employee by the specified ID.<br /><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
read_employee_by_id_response = hibob.people.read_employee_by_id(
    identifier="identifier_example",
    fields=[
        "fields_example"
    ],
    human_readable=False,
    include_human_readable=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### identifier: `str`<a id="identifier-str"></a>

employee id

##### fields: List[`str`]<a id="fields-liststr"></a>

Whether to supply fields (paths) instead of empty list as a default in order  to not exceed data permitted.

##### human_readable: `bool`<a id="human_readable-bool"></a>

Whether to supply humanReadable values in JSON instead of machine-readable (default) format.

##### include_human_readable: `bool`<a id="include_human_readable-bool"></a>

Whether to include the additional \"humanReadable\" JSON node in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`Employees`](./hi_bob_python_sdk/pydantic/employees.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{identifier}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.read_employee_fields`<a id="hibobpeopleread_employee_fields"></a>

<b>Note:</b> Changes to this API are planned to take effect on May 31, 2024.  Make sure to review all of the details in the <a href='https://help.hibob.com/hc/en-us/articles/19726260483601'>Working pattern API Changes</a>  article in the help center.<br> <br>Returns the employee's fields by the specified ID or email.<br /><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
read_employee_fields_response = hibob.people.read_employee_fields(
    identifier="identifier_example",
    fields=["root.id", "root.firstName", "root.surname", "root.email", "work.site", "work.department"],
    human_readable="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### identifier: `str`<a id="identifier-str"></a>

employee ID or email

##### fields: [`ReadSingleEmployeeRequestReferenceFields`](./hi_bob_python_sdk/type/read_single_employee_request_reference_fields.py)<a id="fields-readsingleemployeerequestreferencefieldshi_bob_python_sdktyperead_single_employee_request_reference_fieldspy"></a>

##### human_readable: `str`<a id="human_readable-str"></a>

Optional field.  <br> <b>If not sent:</b> supply machine-readable values only. <br> <br> Possible values: <br>  <br> <b>APPEND</b> - include the additional \\\"humanReadable\\\" JSON node in the response. <br>  <br> <b>REPLACE</b> - supply humanReadable values in JSON instead of machine-readable format. <br>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReadSingleEmployeeRequestReference`](./hi_bob_python_sdk/type/read_single_employee_request_reference.py)
Read request content that allows you to select fields and other options

#### 🔄 Return<a id="🔄-return"></a>

[`Employees`](./hi_bob_python_sdk/pydantic/employees.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{identifier}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.revoke_access_to_employee`<a id="hibobpeoplerevoke_access_to_employee"></a>

Revoke access to Bob for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.revoke_access_to_employee(
    identifier="identifier_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### identifier: `str`<a id="identifier-str"></a>

employee id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{identifier}/uninvite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.search_employees`<a id="hibobpeoplesearch_employees"></a>

<b>Note:</b> Changes to this API are planned to take effect on May 31, 2024.  Make sure to review all of the details in the <a href='https://help.hibob.com/hc/en-us/articles/19726260483601'>Working pattern API Changes</a>  article in the help center.<br> <br>This API returns a list of requested employees with requested fields.  The data is filtered based on the requested fields and access level of the logged-in user.  Only viewable categories are returned.<br /> <br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_employees_response = hibob.people.search_employees(
    fields=["root.id", "root.firstName", "root.surname", "root.email", "work.site", "work.department"],
    filters=[
        {
            "field_path": "root.id",
            "operator": "equals",
            "values": ["employeeId1", "employeeId2", "employeeId3"],
        }
    ],
    show_inactive=True,
    human_readable="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: [`ReadEmployeesRequestReferenceFields`](./hi_bob_python_sdk/type/read_employees_request_reference_fields.py)<a id="fields-reademployeesrequestreferencefieldshi_bob_python_sdktyperead_employees_request_reference_fieldspy"></a>

##### filters: List[`EmployeeFilter`]<a id="filters-listemployeefilter"></a>

Optional list of filters for filtering employees. We currently support up to one filter.

##### show_inactive: `bool`<a id="show_inactive-bool"></a>

<br>Optional field. <br>Default value = false. <br>Defines whether response should include inactive employees.

##### human_readable: `str`<a id="human_readable-str"></a>

Optional field.  <br> <b>If not sent:</b> supply machine-readable values only. <br> <br> Possible values: <br>  <br> <b>APPEND</b> - include the additional \\\"humanReadable\\\" JSON node in the response. <br>  <br> <b>REPLACE</b> - supply humanReadable values in JSON instead of machine-readable format. <br>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReadEmployeesRequestReference`](./hi_bob_python_sdk/type/read_employees_request_reference.py)
Read request content that allows you to select fields and other options

#### 🔄 Return<a id="🔄-return"></a>

[`Employees`](./hi_bob_python_sdk/pydantic/employees.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/search` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.set_start_date`<a id="hibobpeopleset_start_date"></a>

Set or update an employee's start date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.set_start_date(
    start_date="1970-01-01",
    employee_id="employeeId_example",
    reason="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `date`<a id="start_date-date"></a>

The date this entry becomes effective.

##### employee_id: `str`<a id="employee_id-str"></a>

employee ID

##### reason: `str`<a id="reason-str"></a>

Additional info for the start date update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StartDateUpdate`](./hi_bob_python_sdk/type/start_date_update.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/start-date` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.terminate_employee`<a id="hibobpeopleterminate_employee"></a>

This changes the employee’s status to Terminated according to specified termination date. <br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.terminate_employee(
    termination_date="Mon Sep 22 17:00:00 PDT 2025",
    identifier="identifier_example",
    termination_reason="Redundant",
    reason_type="End of Contract",
    notice_period={
        "unit": "days",
        "length": 30,
    },
    last_day_of_work="Sun Sep 21 17:00:00 PDT 2025",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### termination_date: `date`<a id="termination_date-date"></a>

The employee's termination date

##### identifier: `str`<a id="identifier-str"></a>

Employee ID.

##### termination_reason: `str`<a id="termination_reason-str"></a>

The ID of the 'terminationReason' list entry

##### reason_type: `str`<a id="reason_type-str"></a>

The ID of the 'lifecycleReasonType' list entry

##### notice_period: [`EmployeeTerminationNoticePeriod`](./hi_bob_python_sdk/type/employee_termination_notice_period.py)<a id="notice_period-employeeterminationnoticeperiodhi_bob_python_sdktypeemployee_termination_notice_periodpy"></a>


##### last_day_of_work: `date`<a id="last_day_of_work-date"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeTermination`](./hi_bob_python_sdk/type/employee_termination.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{identifier}/terminate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.update_email`<a id="hibobpeopleupdate_email"></a>

Change an employee's email address. If you cannot change the self email an invitation will be sent to the new address to verify the email if the employee is invited/active.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.update_email(
    id="id_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

employee id

##### email: `str`<a id="email-str"></a>

new email

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeEmail`](./hi_bob_python_sdk/type/change_email.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/email` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.update_employee_record`<a id="hibobpeopleupdate_employee_record"></a>

<b>Note:</b> Changes to this API are planned to take effect on May 31, 2024.  Make sure to review all of the details in the <a href='https://help.hibob.com/hc/en-us/articles/19726260483601'>Working pattern API Changes</a>  article in the help center.<br> <br>This updates the employee record in Bob. You can include only the fields listed in the  [Fields Metadata API](https://apidocs.hibob.com/reference/get_company-people-fields) where historical is equal to false.  <br /><br><b>Note</b>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.update_employee_record(
    identifier="identifier_example",
    first_name="Bob",
    personal={
        "birth_date": "2002-01-01",
    },
    about={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### identifier: `str`<a id="identifier-str"></a>

Employee ID.

##### first_name: `str`<a id="first_name-str"></a>

##### personal: [`PeopleUpdateEmployeeRecordRequestPersonal`](./hi_bob_python_sdk/type/people_update_employee_record_request_personal.py)<a id="personal-peopleupdateemployeerecordrequestpersonalhi_bob_python_sdktypepeople_update_employee_record_request_personalpy"></a>


##### about: [`PeopleUpdateEmployeeRecordRequestAbout`](./hi_bob_python_sdk/type/people_update_employee_record_request_about.py)<a id="about-peopleupdateemployeerecordrequestabouthi_bob_python_sdktypepeople_update_employee_record_request_aboutpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleUpdateEmployeeRecordRequest`](./hi_bob_python_sdk/type/people_update_employee_record_request.py)
Use Fields Metadata API for available field definitions

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{identifier}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.update_employment_entry`<a id="hibobpeopleupdate_employment_entry"></a>

<br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.update_employment_entry(
    body=None,
    effective_date="1970-01-01",
    id="id_example",
    entry_id=1,
    id=1,
    reason="string_example",
    contract="string_example",
    type="string_example",
    salary_pay_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to update.

##### requestBody: [`EmploymentEntry`](./hi_bob_python_sdk/type/employment_entry.py)<a id="requestbody-employmententryhi_bob_python_sdktypeemployment_entrypy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/employment/{entry_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.update_equity_grant_for_employee`<a id="hibobpeopleupdate_equity_grant_for_employee"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>. - Basic: [] - Bearer: []

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.update_equity_grant_for_employee(
    body=None,
    quantity=3.14,
    equity_type="string_example",
    id="id_example",
    entry_id=1,
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    vesting_commencement_date="1970-01-01",
    consent_number="string_example",
    grant_date="1970-01-01",
    option_expiration="1970-01-01",
    exercise_price={
        "value": 3.14,
        "currency": "currency_example",
    },
    vesting_term="string_example",
    grant_type="string_example",
    vesting_schedule=3.14,
    grant_number=3.14,
    grant_status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to update.

##### requestBody: [`EquityEntry`](./hi_bob_python_sdk/type/equity_entry.py)<a id="requestbody-equityentryhi_bob_python_sdktypeequity_entrypy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities/{entry_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.update_work_entry`<a id="hibobpeopleupdate_work_entry"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.update_work_entry(
    body=None,
    id="id_example",
    entry_id=1,
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    title="string_example",
    department="string_example",
    site="string_example",
    site_id=1,
    reports_to={
        "id": "id_example",
    },
    custom_columns={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to update.

##### requestBody: [`WorkEntry`](./hi_bob_python_sdk/type/work_entry.py)<a id="requestbody-workentryhi_bob_python_sdktypework_entrypy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/work/{entry_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.people.upload_employee_avatar_url`<a id="hibobpeopleupload_employee_avatar_url"></a>

Upload an employee's Avatar by providing a URL to the image to upload.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.people.upload_employee_avatar_url(
    url="string_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

The URL of the source of the avatar image.

##### employee_id: `str`<a id="employee_id-str"></a>

Employee ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadAvatar`](./hi_bob_python_sdk/type/upload_avatar.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/{employeeId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.reports.download_by_id`<a id="hibobreportsdownload_by_id"></a>

Returns a report data file in the specified format.<br /><b>Supported user types:</b> Service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_by_id_response = hibob.reports.download_by_id(
    report_id=3.14,
    format="csv",
    include_info=True,
    locale="string_example",
    human_readable="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### report_id: `Union[int, float]`<a id="report_id-unionint-float"></a>

Report ID

##### format: `str`<a id="format-str"></a>

File format

##### include_info: `bool`<a id="include_info-bool"></a>

Should include info.

##### locale: `str`<a id="locale-str"></a>

Requested language for the report columns in the format of locale (e.g. fr-FR). If this is not provided, the user preferences locale is used.

##### human_readable: `str`<a id="human_readable-str"></a>

Optional field. Only enforced when <i><b>format</b></i> is <i>json</i>. <br> <b>If not sent:</b> supply machine-readable values only. <br> <br> Possible values: <br>  <br> <b>APPEND</b> - include the additional \"humanReadable\" JSON node in the response. <br>  <br> <b>REPLACE</b> - supply humanReadable values in JSON instead of machine-readable format. <br>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/reports/{reportId}/download` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.reports.download_report_file`<a id="hibobreportsdownload_report_file"></a>

Returns the report data file when it is ready. If the file is not ready yet the response will be 204. It will then have to try again.<br />(This URL is the response of the previous API: https://api.hibob.com/v1/company/reports/reportId/download-async)<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_report_file_response = hibob.reports.download_report_file(
    report_name="reportName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### report_name: `str`<a id="report_name-str"></a>

Report name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/reports/download/{reportName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.reports.get_download_url`<a id="hibobreportsget_download_url"></a>

Returns the polling URL report file of the specified format under "Location" in the response header.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.reports.get_download_url(
    report_id=3.14,
    format="csv",
    include_info=True,
    locale="string_example",
    human_readable="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### report_id: `Union[int, float]`<a id="report_id-unionint-float"></a>

Report id

##### format: `str`<a id="format-str"></a>

File format

##### include_info: `bool`<a id="include_info-bool"></a>

Should include info

##### locale: `str`<a id="locale-str"></a>

Requested language for the report columns in the format of the locale (e.g. fr-FR). If this is not provided, the user preferences locale is used.

##### human_readable: `str`<a id="human_readable-str"></a>

Optional field. Only enforced when <i><b>format</b></i> is <i>json</i>. <br> <b>If not sent:</b> supply machine-readable values only. <br> <br> Possible values: <br>  <br> <b>APPEND</b> - include the additional \"humanReadable\" JSON node in the response. <br>  <br> <b>REPLACE</b> - supply humanReadable values in JSON instead of machine-readable format. <br>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/reports/{reportId}/download-async` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.reports.list_accessible_reports`<a id="hibobreportslist_accessible_reports"></a>

Returns a list of all the defined company reports. The data is filtered based on the access level of the user. Only viewable categories are returned.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_accessible_reports_response = hibob.reports.list_accessible_reports()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Reports`](./hi_bob_python_sdk/pydantic/reports.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/reports` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.create_employment_entry`<a id="hibobtablescreate_employment_entry"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.create_employment_entry(
    body=None,
    effective_date="1970-01-01",
    id="id_example",
    id=1,
    reason="string_example",
    contract="string_example",
    type="string_example",
    salary_pay_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

employee id

##### requestBody: [`EmploymentEntry`](./hi_bob_python_sdk/type/employment_entry.py)<a id="requestbody-employmententryhi_bob_python_sdktypeemployment_entrypy"></a>

Employment entry to add. This must not conflict with another entry on the same effective date.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/employment` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.create_equity_grant`<a id="hibobtablescreate_equity_grant"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.create_equity_grant(
    body=None,
    quantity=3.14,
    equity_type="string_example",
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    vesting_commencement_date="1970-01-01",
    consent_number="string_example",
    grant_date="1970-01-01",
    option_expiration="1970-01-01",
    exercise_price={
        "value": 3.14,
        "currency": "currency_example",
    },
    vesting_term="string_example",
    grant_type="string_example",
    vesting_schedule=3.14,
    grant_number=3.14,
    grant_status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`EquityEntry`](./hi_bob_python_sdk/type/equity_entry.py)<a id="requestbody-equityentryhi_bob_python_sdktypeequity_entrypy"></a>

Equity grant to add.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.create_new_salary_entry`<a id="hibobtablescreate_new_salary_entry"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.create_new_salary_entry(
    body=None,
    base={
        "value": 3.14,
        "currency": "currency_example",
    },
    pay_period="string_example",
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    pay_frequency="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`SalaryEntry`](./hi_bob_python_sdk/type/salary_entry.py)<a id="requestbody-salaryentryhi_bob_python_sdktypesalary_entrypy"></a>

Salary entry to add. This must not conflict with another entry on the same effective date.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/salaries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.create_training_record`<a id="hibobtablescreate_training_record"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.create_training_record(
    body=None,
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    description="string_example",
    name="string_example",
    cost={
        "value": 3.14,
        "currency": "currency_example",
    },
    status="string_example",
    frequency="string_example",
    start_date="1970-01-01",
    end_date="1970-01-01",
    document_id=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`TrainingEntry`](./hi_bob_python_sdk/type/training_entry.py)<a id="requestbody-trainingentryhi_bob_python_sdktypetraining_entrypy"></a>

Training entry to add.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/training` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.create_variable_payment`<a id="hibobtablescreate_variable_payment"></a>

<br><br><b>Note</b>:The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.create_variable_payment(
    body=None,
    amount={
        "value": 3.14,
        "currency": "currency_example",
    },
    payment_period="string_example",
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    variable_type="string_example",
    company_percent=3.14,
    department_percent=3.14,
    individual_percent=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`VariableEntry`](./hi_bob_python_sdk/type/variable_entry.py)<a id="requestbody-variableentryhi_bob_python_sdktypevariable_entrypy"></a>

Variable payment to add.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/variable` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.create_work_entry`<a id="hibobtablescreate_work_entry"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.create_work_entry(
    body=None,
    id="id_example",
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    title="string_example",
    department="string_example",
    site="string_example",
    site_id=1,
    reports_to={
        "id": "id_example",
    },
    custom_columns={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### requestBody: [`WorkEntry`](./hi_bob_python_sdk/type/work_entry.py)<a id="requestbody-workentryhi_bob_python_sdktypework_entrypy"></a>

Work entry to add. This must not conflict with another entry on the same effective date.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/work` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.delete_employment_entry`<a id="hibobtablesdelete_employment_entry"></a>

Deletes an employment entry from a given employee's employment history.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.delete_employment_entry(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/employment/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.delete_equity_grant`<a id="hibobtablesdelete_equity_grant"></a>

Deletes an equity grant for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.delete_equity_grant(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The Entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.delete_salary_entry`<a id="hibobtablesdelete_salary_entry"></a>

Deletes a salary entry from the employee's list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.delete_salary_entry(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/salaries/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.delete_training_record`<a id="hibobtablesdelete_training_record"></a>

Deletes a training record for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.delete_training_record(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The Entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/variable/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.delete_training_record_0`<a id="hibobtablesdelete_training_record_0"></a>

Deletes any training records for an employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.delete_training_record_0(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The Entry ID to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/training/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.delete_work_entry`<a id="hibobtablesdelete_work_entry"></a>

Deletes a work entry from a given employee's work history.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.delete_work_entry(
    id="id_example",
    entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/work/{entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.get_employment_history`<a id="hibobtablesget_employment_history"></a>

<b>Note:</b> Changes to this API are planned to take effect on May 31, 2024.  Make sure to review all of the details in the <a href='https://help.hibob.com/hc/en-us/articles/19726260483601'>Working pattern API Changes</a>  article in the help center.<br> <br>Returns a list of employment history entries for a given employee.<br /><br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employment_history_response = hibob.tables.get_employment_history(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

employee id

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentEntries`](./hi_bob_python_sdk/pydantic/employment_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/employment` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.get_salary_history`<a id="hibobtablesget_salary_history"></a>

Returns a list of salary history entries for a given employee.<br /><br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_salary_history_response = hibob.tables.get_salary_history(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`SalaryEntries`](./hi_bob_python_sdk/pydantic/salary_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/salaries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.get_work_history`<a id="hibobtablesget_work_history"></a>

Returns a list of work history entries for a given employee.<br /><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_history_response = hibob.tables.get_work_history(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkEntries`](./hi_bob_python_sdk/pydantic/work_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/work` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.list_employee_lifecycle`<a id="hibobtableslist_employee_lifecycle"></a>

Returns a list of life-cycle history entries for a given employee.<br /><br><br><b>Note</b>: TThe values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employee_lifecycle_response = hibob.tables.list_employee_lifecycle(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`LifeCycleEntries`](./hi_bob_python_sdk/pydantic/life_cycle_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/lifecycle` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.list_equity_grants`<a id="hibobtableslist_equity_grants"></a>

Returns a list of equity grants for a given employee.<br /><b>Supported user types:</b> Service<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_equity_grants_response = hibob.tables.list_equity_grants(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`EquityEntries`](./hi_bob_python_sdk/pydantic/equity_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.list_training_records`<a id="hibobtableslist_training_records"></a>

Returns a list of training records for a given employee<br /><br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_training_records_response = hibob.tables.list_training_records(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`TrainingEntries`](./hi_bob_python_sdk/pydantic/training_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/training` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.list_variable_payments`<a id="hibobtableslist_variable_payments"></a>

Returns a list of variable payments for a given employee.<br /><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_variable_payments_response = hibob.tables.list_variable_payments(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`VariableEntries`](./hi_bob_python_sdk/pydantic/variable_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/variable` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.update_employment_entry`<a id="hibobtablesupdate_employment_entry"></a>

<br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.update_employment_entry(
    body=None,
    effective_date="1970-01-01",
    id="id_example",
    entry_id=1,
    id=1,
    reason="string_example",
    contract="string_example",
    type="string_example",
    salary_pay_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to update.

##### requestBody: [`EmploymentEntry`](./hi_bob_python_sdk/type/employment_entry.py)<a id="requestbody-employmententryhi_bob_python_sdktypeemployment_entrypy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/employment/{entry_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.update_equity_grant_for_employee`<a id="hibobtablesupdate_equity_grant_for_employee"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>. - Basic: [] - Bearer: []

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.update_equity_grant_for_employee(
    body=None,
    quantity=3.14,
    equity_type="string_example",
    id="id_example",
    entry_id=1,
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    vesting_commencement_date="1970-01-01",
    consent_number="string_example",
    grant_date="1970-01-01",
    option_expiration="1970-01-01",
    exercise_price={
        "value": 3.14,
        "currency": "currency_example",
    },
    vesting_term="string_example",
    grant_type="string_example",
    vesting_schedule=3.14,
    grant_number=3.14,
    grant_status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to update.

##### requestBody: [`EquityEntry`](./hi_bob_python_sdk/type/equity_entry.py)<a id="requestbody-equityentryhi_bob_python_sdktypeequity_entrypy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/equities/{entry_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tables.update_work_entry`<a id="hibobtablesupdate_work_entry"></a>

<br><br><b>Note</b>: The values of the list fields represent the list item ID and not the list item value. To obtain the corresponding list item value, use the HiBob metadata API to determine the field list name. Then, use the list item ID to locate the list item value. For more information, see <a href='https://apidocs.hibob.com/docs/how-to-work-with-lists-public-api'>How to work with lists Public API</a>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.tables.update_work_entry(
    body=None,
    id="id_example",
    entry_id=1,
    id=1,
    reason="string_example",
    effective_date="1970-01-01",
    title="string_example",
    department="string_example",
    site="string_example",
    site_id=1,
    reports_to={
        "id": "id_example",
    },
    custom_columns={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### entry_id: `int`<a id="entry_id-int"></a>

The entry ID to update.

##### requestBody: [`WorkEntry`](./hi_bob_python_sdk/type/work_entry.py)<a id="requestbody-workentryhi_bob_python_sdktypework_entrypy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{id}/work/{entry_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tasks.complete_task`<a id="hibobtaskscomplete_task"></a>

Mark a task as complete

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_task_response = hibob.tasks.complete_task(
    task_id="taskId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_id: `str`<a id="task_id-str"></a>

task id

#### 🔄 Return<a id="🔄-return"></a>

[`Tasks`](./hi_bob_python_sdk/pydantic/tasks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{taskId}/complete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tasks.get_employee_tasks`<a id="hibobtasksget_employee_tasks"></a>

<b>Supported user types:</b> Employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_tasks_response = hibob.tasks.get_employee_tasks()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Tasks`](./hi_bob_python_sdk/pydantic/tasks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/my/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tasks.get_open_tasks`<a id="hibobtasksget_open_tasks"></a>

Read all open tasks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_open_tasks_response = hibob.tasks.get_open_tasks()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Tasks`](./hi_bob_python_sdk/pydantic/tasks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.tasks.read_employee_tasks`<a id="hibobtasksread_employee_tasks"></a>

Read tasks of a specific employee 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
read_employee_tasks_response = hibob.tasks.read_employee_tasks(
    id="id_example",
    task_status="open",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

employee id

##### task_status: `str`<a id="task_status-str"></a>

filter tasks by open / closed status. Not sending task_status will return all tasks.

#### 🔄 Return<a id="🔄-return"></a>

[`Tasks`](./hi_bob_python_sdk/pydantic/tasks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/people/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.add_reason_codes`<a id="hibobtime_offadd_reason_codes"></a>

Add a list of reason codes for a given policy type.<br /><b>Supported user types:</b> Service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.time_off.add_reason_codes(
    policy_type="policyType_example",
    reason_codes=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_type: `str`<a id="policy_type-str"></a>

Policy Type name

##### reason_codes: [`ReasonCodesNamesReasonCodes`](./hi_bob_python_sdk/type/reason_codes_names_reason_codes.py)<a id="reason_codes-reasoncodesnamesreasoncodeshi_bob_python_sdktypereason_codes_names_reason_codespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReasonCodesNames`](./hi_bob_python_sdk/type/reason_codes_names.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/policy-types/{policyType}/reason-codes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.cancel_request`<a id="hibobtime_offcancel_request"></a>

Cancels an existing time off request.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.time_off.cancel_request(
    id="id_example",
    request_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### request_id: `int`<a id="request_id-int"></a>

Request ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/employees/{id}/requests/{requestId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.create_balance_adjustment`<a id="hibobtime_offcreate_balance_adjustment"></a>

Create a balance adjustment for a given employee for a given effective date.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.time_off.create_balance_adjustment(
    id="id_example",
    adjustment_type="balance",
    policy_type="string_example",
    effective_date="1970-01-01",
    amount=3.14,
    reason="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### adjustment_type: `str`<a id="adjustment_type-str"></a>

Adjustment type - balance or time used.

##### policy_type: `str`<a id="policy_type-str"></a>

Policy type name.

##### effective_date: `date`<a id="effective_date-date"></a>

The date this adjustment becomes effective.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount of days/hours to add/subtract.

##### reason: `str`<a id="reason-str"></a>

A reason for this adjustment.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AdjustmentRequest`](./hi_bob_python_sdk/type/adjustment_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/employees/{id}/adjustments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.get_details_of_request`<a id="hibobtime_offget_details_of_request"></a>

Supplies detailed info about an existing time off request.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_of_request_response = hibob.time_off.get_details_of_request(
    id="id_example",
    request_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

employee id

##### request_id: `int`<a id="request_id-int"></a>

request id

#### 🔄 Return<a id="🔄-return"></a>

[`TimeoffRequest`](./hi_bob_python_sdk/pydantic/timeoff_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/employees/{id}/requests/{requestId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.get_employee_balance`<a id="hibobtime_offget_employee_balance"></a>

Retrieve the balance for a given employee, for a given policy type, as of a given date.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_balance_response = hibob.time_off.get_employee_balance(
    id="id_example",
    policy_type="policyType_example",
    date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### policy_type: `str`<a id="policy_type-str"></a>

Policy type name.

##### date: `date`<a id="date-date"></a>

Point in time.

#### 🔄 Return<a id="🔄-return"></a>

[`BalanceResult`](./hi_bob_python_sdk/pydantic/balance_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/employees/{id}/balance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.get_new_deleted_requests_since_date`<a id="hibobtime_offget_new_deleted_requests_since_date"></a>

Returns the list of time off requests that are pending, approved or canceled since the specified date.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_new_deleted_requests_since_date_response = hibob.time_off.get_new_deleted_requests_since_date(
    since="1970-01-01",
    include_pending=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### since: `date`<a id="since-date"></a>

Timestamp starting from which to return the changes. Should be in ISO-8601 format, e.g. 2050-04-05T14:30:24.345Z or 2050-04-05T12:30-02:00.

##### include_pending: `bool`<a id="include_pending-bool"></a>

Optional parameter. Indicates whether to include pending requests in the results.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeoffChanges`](./hi_bob_python_sdk/pydantic/timeoff_changes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/requests/changes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.get_out_of_office`<a id="hibobtime_offget_out_of_office"></a>

Returns the list of people that have a time off request today or on the specified date.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_out_of_office_response = hibob.time_off.get_out_of_office(
    today="1970-01-01",
    include_hourly=False,
    include_private=False,
    site_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### today: `date`<a id="today-date"></a>

Date to report out of the office. If not specified, the date at UTC at the time of the request is used.

##### include_hourly: `bool`<a id="include_hourly-bool"></a>

Include Hourly Requests

##### include_private: `bool`<a id="include_private-bool"></a>

Show the policy type's name instead of the policy's custom public name if the user has permission to view it, and the policy's custom public name exists.

##### site_id: `int`<a id="site_id-int"></a>

The employee's site ID

#### 🔄 Return<a id="🔄-return"></a>

[`OutTodays`](./hi_bob_python_sdk/pydantic/out_todays.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/outtoday` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.get_policy_details`<a id="hibobtime_offget_policy_details"></a>

Get details about a given policy type.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_details_response = hibob.time_off.get_policy_details(
    policy_type="policyType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_type: `str`<a id="policy_type-str"></a>

Policy Type name

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyType`](./hi_bob_python_sdk/pydantic/policy_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/policy-types/{policyType}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.get_policy_details_0`<a id="hibobtime_offget_policy_details_0"></a>

Get details about a given policy.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_details_0_response = hibob.time_off.get_policy_details_0(
    policy_name="policyName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_name: `str`<a id="policy_name-str"></a>

Policy name.

#### 🔄 Return<a id="🔄-return"></a>

[`Policy`](./hi_bob_python_sdk/pydantic/policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.get_whos_out`<a id="hibobtime_offget_whos_out"></a>

Returns time off information for a given date range.<br /><b>Supported user types:</b> Service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_whos_out_response = hibob.time_off.get_whos_out(
    _from="1970-01-01",
    to="1970-01-01",
    include_hourly=False,
    include_private=False,
    include_pending=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `date`<a id="_from-date"></a>

Start period date

##### to: `date`<a id="to-date"></a>

End period date

##### include_hourly: `bool`<a id="include_hourly-bool"></a>

Include Hourly Requests

##### include_private: `bool`<a id="include_private-bool"></a>

Show the policy type's name instead of the policy's custom public name if the user has permission to view it, and the policy's custom public name exists.

##### include_pending: `bool`<a id="include_pending-bool"></a>

Include Pending Requests

#### 🔄 Return<a id="🔄-return"></a>

[`Requests`](./hi_bob_python_sdk/pydantic/requests.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/whosout` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.list_policy_type_names`<a id="hibobtime_offlist_policy_type_names"></a>

Get a list of policy names for the user's defined policy type.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_policy_type_names_response = hibob.time_off.list_policy_type_names(
    policy_type_name="policyTypeName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_type_name: `str`<a id="policy_type_name-str"></a>

Policy type name.

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyNames`](./hi_bob_python_sdk/pydantic/policy_names.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/policies/names` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.list_policy_types_names`<a id="hibobtime_offlist_policy_types_names"></a>

Get a list of all policy type names.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_policy_types_names_response = hibob.time_off.list_policy_types_names()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyTypes`](./hi_bob_python_sdk/pydantic/policy_types.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/policy-types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.list_reason_codes`<a id="hibobtime_offlist_reason_codes"></a>

Get list of reason codes for a given policy type.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_reason_codes_response = hibob.time_off.list_reason_codes(
    policy_type="policyType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_type: `str`<a id="policy_type-str"></a>

Policy Type name.

#### 🔄 Return<a id="🔄-return"></a>

[`ReasonCodes`](./hi_bob_python_sdk/pydantic/reason_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/policy-types/{policyType}/reason-codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.submit_new_request`<a id="hibobtime_offsubmit_new_request"></a>

Submits a new timeoff request.<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.time_off.submit_new_request(
    policy_type="string_example",
    start_date="1970-01-01",
    id="id_example",
    description="string_example",
    request_range_type="days",
    start_date_portion="all_day",
    end_date="1970-01-01",
    hours=1,
    minutes=1,
    end_date_portion="all_day",
    day_portion="morning",
    daily_hours=1,
    daily_minutes=1,
    skip_manager_approval=False,
    approver="string_example",
    reason_code=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_type: `str`<a id="policy_type-str"></a>

Request policy type, e.g. Holiday, Sick or any custom type defined.

##### start_date: `date`<a id="start_date-date"></a>

Date of the first day of the time off (not relevant for requests using the hours type).

##### id: `str`<a id="id-str"></a>

Employee ID.

##### description: `str`<a id="description-str"></a>

Request reason.

##### request_range_type: `str`<a id="request_range_type-str"></a>

The type of request duration.<br> Select <b>hours</b> when the request is for X hours during the day requested (This is supported only for policy types measured in hours).<br> Select <b>portionOnRange</b> when the  request is for every morning or every afternoon during the days requested.<br> Select <b>hoursOnRange</b> when the request is for X hours every day during the days requested (This is supported only for policy types measured in hours)

##### start_date_portion: `str`<a id="start_date_portion-str"></a>

Portion of the first day - relevant for requests in days.

##### end_date: `date`<a id="end_date-date"></a>

Date of the last day of the time off (not relevant for requests using                                                the hours type).

##### hours: `int`<a id="hours-int"></a>

This field is mandatory if the requestRangeType is set to 'hours'.

##### minutes: `int`<a id="minutes-int"></a>

Relevant if requestRangeType is set to 'hours'.

##### end_date_portion: `str`<a id="end_date_portion-str"></a>

Portion of the last day - relevant for requests in days.

##### day_portion: `str`<a id="day_portion-str"></a>

Select <b>morning</b> when the request is for mornings on the days requested. Select <b>afternoon</b> when the request is for afternoons on the days requested.<br> This is mandatory if the <b>requestRangeType</b> is <b>portionOnRange</b>.

##### daily_hours: `int`<a id="daily_hours-int"></a>

Enter the number of hours when the request is for X hours on the days requested.<br> This is mandatory if the <b>requestRangeType</b> is <b>hoursOnRange</b>.

##### daily_minutes: `int`<a id="daily_minutes-int"></a>

Enter the number of minutes when the request is for X hours and X minutes on the days requested.<br> This is relevant if the <b>requestRangeType</b> is <b>hoursOnRange</b> and the amount requested is not a full hour or hours.

##### skip_manager_approval: `bool`<a id="skip_manager_approval-bool"></a>

Admins only can skip the approval policy. Setting this field to true will create an approved request.

##### approver: `str`<a id="approver-str"></a>

The employee ID of the user to be set as the approver for this request. This is relevant if 'skipManagerApproval' is set to true.<br>Please note that the user calling the API with this param must have permission to import time off requests.

##### reason_code: `int`<a id="reason_code-int"></a>

The reason code ID taken from the policy type's reason codes list. The list is available in GET /timeoff/policy-types/{policyType}/reason-codes

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubmitTimeoffRequest`](./hi_bob_python_sdk/type/submit_timeoff_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/employees/{id}/requests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `hibob.time_off.submit_new_request_diff_hours`<a id="hibobtime_offsubmit_new_request_diff_hours"></a>

Submits a new timeoff request of different hours per day.<br /><b>Supported user types:</b> Employee, Service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hibob.time_off.submit_new_request_diff_hours(
    policy_type="Holiday",
    start_date="2024-01-03",
    end_date="2024-01-05",
    durations=[{
    "date": "1970-01-01",
    "hours": 1,
    "minutes": 1,
}, , ],
    id="id_example",
    description="Vacation",
    skip_manager_approval=False,
    approver="3452152476387906847",
    reason_code=3000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_type: `str`<a id="policy_type-str"></a>

Request policy type, e.g. Holiday, Sick or any custom type defined.

##### start_date: `date`<a id="start_date-date"></a>

Date of the first day of the time off

##### end_date: `date`<a id="end_date-date"></a>

Date of the last day of the time off.

##### durations: [`SubmitTimeoffRequestDiffHoursDurations`](./hi_bob_python_sdk/type/submit_timeoff_request_diff_hours_durations.py)<a id="durations-submittimeoffrequestdiffhoursdurationshi_bob_python_sdktypesubmit_timeoff_request_diff_hours_durationspy"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

##### description: `str`<a id="description-str"></a>

Request reason.

##### skip_manager_approval: `bool`<a id="skip_manager_approval-bool"></a>

Admins only can skip the approval policy. Setting this field to true will create an approved request.

##### approver: `str`<a id="approver-str"></a>

The employee ID of the user to be set as the approver for this request. This is relevant if 'skipManagerApproval' is set to true.<br>Please note that the user calling the API with this param must have permission to import time off requests.

##### reason_code: `int`<a id="reason_code-int"></a>

The reason code ID taken from the policy type's reason codes list. The list is available in GET /timeoff/policy-types/{policyType}/reason-codes

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubmitTimeoffRequestDiffHours`](./hi_bob_python_sdk/type/submit_timeoff_request_diff_hours.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timeoff/employees/{id}/diffHours/requests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
