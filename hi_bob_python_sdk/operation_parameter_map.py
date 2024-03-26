operation_parameter_map = {
    '/attendance/import/{importMethod}-POST': {
        'parameters': [
            {
                'name': 'idType'
            },
            {
                'name': 'requests'
            },
            {
                'name': 'importMethod'
            },
            {
                'name': 'dateTimeFormat'
            },
        ]
    },
    '/people/custom-tables/{employee_id}/{custom_table_id}-POST': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'custom_table_id'
            },
            {
                'name': 'RAW_BODY'
            },
        ]
    },
    '/people/custom-tables/{employee_id}/{custom_table_id}/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'custom_table_id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/custom-tables/{employee_id}/{custom_table_id}-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'custom_table_id'
            },
            {
                'name': 'includeHumanReadable'
            },
        ]
    },
    '/people/custom-tables/{employee_id}/{custom_table_id}/{entry_id}-PUT': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'custom_table_id'
            },
            {
                'name': 'entry_id'
            },
            {
                'name': 'RAW_BODY'
            },
        ]
    },
    '/docs/people/{id}/confidential/{docId}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'docId'
            },
        ]
    },
    '/docs/people/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/docs/people/{id}/shared/{docId}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'docId'
            },
        ]
    },
    '/docs/people/{id}/confidential/upload-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/docs/people/{id}/confidential-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'documentName'
            },
            {
                'name': 'documentUrl'
            },
        ]
    },
    '/docs/people/{id}/shared-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'documentName'
            },
            {
                'name': 'documentUrl'
            },
        ]
    },
    '/docs/people/{id}/shared/upload-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/company/people/fields-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'category'
            },
            {
                'name': 'type'
            },
            {
                'name': 'description'
            },
            {
                'name': 'historical'
            },
        ]
    },
    '/company/named-lists/{listName}-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'listName'
            },
            {
                'name': 'parentId'
            },
        ]
    },
    '/company/people/fields/{fieldId}-DELETE': {
        'parameters': [
            {
                'name': 'fieldId'
            },
        ]
    },
    '/company/named-lists/{listName}/{itemId}-DELETE': {
        'parameters': [
            {
                'name': 'listName'
            },
            {
                'name': 'itemId'
            },
        ]
    },
    '/company/people/fields-GET': {
        'parameters': [
        ]
    },
    '/company/named-lists-GET': {
        'parameters': [
            {
                'name': 'includeArchived'
            },
        ]
    },
    '/people/custom-tables/metadata-GET': {
        'parameters': [
        ]
    },
    '/company/named-lists/{listName}-GET': {
        'parameters': [
            {
                'name': 'listName'
            },
            {
                'name': 'includeArchived'
            },
        ]
    },
    '/metadata/objects/position-GET': {
        'parameters': [
        ]
    },
    '/people/custom-tables/metadata/{custom_table_id}-GET': {
        'parameters': [
            {
                'name': 'custom_table_id'
            },
        ]
    },
    '/company/people/fields/{fieldId}-PUT': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/company/named-lists/{listName}/{itemId}-PUT': {
        'parameters': [
            {
                'name': 'listName'
            },
            {
                'name': 'itemId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'parentId'
            },
        ]
    },
    '/objects/position/search-POST': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'includeHumanReadable'
            },
        ]
    },
    '/onboarding/wizards-GET': {
        'parameters': [
        ]
    },
    '/people/{id}/equities-POST': {
        'parameters': [
            {
                'name': 'quantity'
            },
            {
                'name': 'equityType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'vestingCommencementDate'
            },
            {
                'name': 'consentNumber'
            },
            {
                'name': 'grantDate'
            },
            {
                'name': 'optionExpiration'
            },
            {
                'name': 'exercisePrice'
            },
            {
                'name': 'vestingTerm'
            },
            {
                'name': 'grantType'
            },
            {
                'name': 'vestingSchedule'
            },
            {
                'name': 'grantNumber'
            },
            {
                'name': 'grantStatus'
            },
        ]
    },
    '/people/{id}/salaries-POST': {
        'parameters': [
            {
                'name': 'base'
            },
            {
                'name': 'payPeriod'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'payFrequency'
            },
        ]
    },
    '/people/{id}/training-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'cost'
            },
            {
                'name': 'status'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'documentId'
            },
        ]
    },
    '/people/{id}/variable-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'paymentPeriod'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'variableType'
            },
            {
                'name': 'companyPercent'
            },
            {
                'name': 'departmentPercent'
            },
            {
                'name': 'individualPercent'
            },
        ]
    },
    '/people/{id}/equities/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/salaries/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/variable/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/training/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/salaries-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/equities-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/training-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/variable-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/payroll/history-GET': {
        'parameters': [
            {
                'name': 'department'
            },
            {
                'name': 'showInactive'
            },
        ]
    },
    '/people/{id}/equities/{entry_id}-PUT': {
        'parameters': [
            {
                'name': 'quantity'
            },
            {
                'name': 'equityType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'vestingCommencementDate'
            },
            {
                'name': 'consentNumber'
            },
            {
                'name': 'grantDate'
            },
            {
                'name': 'optionExpiration'
            },
            {
                'name': 'exercisePrice'
            },
            {
                'name': 'vestingTerm'
            },
            {
                'name': 'grantType'
            },
            {
                'name': 'vestingSchedule'
            },
            {
                'name': 'grantNumber'
            },
            {
                'name': 'grantStatus'
            },
        ]
    },
    '/people-POST': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'surname'
            },
            {
                'name': 'email'
            },
            {
                'name': 'work'
            },
        ]
    },
    '/people/{id}/employment-POST': {
        'parameters': [
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'contract'
            },
            {
                'name': 'type'
            },
            {
                'name': 'salaryPayType'
            },
        ]
    },
    '/people/{id}/equities-POST': {
        'parameters': [
            {
                'name': 'quantity'
            },
            {
                'name': 'equityType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'vestingCommencementDate'
            },
            {
                'name': 'consentNumber'
            },
            {
                'name': 'grantDate'
            },
            {
                'name': 'optionExpiration'
            },
            {
                'name': 'exercisePrice'
            },
            {
                'name': 'vestingTerm'
            },
            {
                'name': 'grantType'
            },
            {
                'name': 'vestingSchedule'
            },
            {
                'name': 'grantNumber'
            },
            {
                'name': 'grantStatus'
            },
        ]
    },
    '/people/{id}/salaries-POST': {
        'parameters': [
            {
                'name': 'base'
            },
            {
                'name': 'payPeriod'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'payFrequency'
            },
        ]
    },
    '/people/{id}/training-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'cost'
            },
            {
                'name': 'status'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'documentId'
            },
        ]
    },
    '/people/{id}/variable-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'paymentPeriod'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'variableType'
            },
            {
                'name': 'companyPercent'
            },
            {
                'name': 'departmentPercent'
            },
            {
                'name': 'individualPercent'
            },
        ]
    },
    '/people/{id}/work-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'title'
            },
            {
                'name': 'department'
            },
            {
                'name': 'site'
            },
            {
                'name': 'siteId'
            },
            {
                'name': 'reportsTo'
            },
            {
                'name': 'customColumns'
            },
        ]
    },
    '/people/{id}/employment/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/equities/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/salaries/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/variable/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/training/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/work/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/avatars/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
        ]
    },
    '/my/avatar-GET': {
        'parameters': [
        ]
    },
    '/avatars-GET': {
        'parameters': [
            {
                'name': 'email'
            },
        ]
    },
    '/people/{id}/employment-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/salaries-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/work-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/employees/{employeeId}/invitations-POST': {
        'parameters': [
            {
                'name': 'welcomeWizardId'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/profiles-GET': {
        'parameters': [
            {
                'name': 'sortBy'
            },
        ]
    },
    '/people/{id}/lifecycle-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people-GET': {
        'parameters': [
            {
                'name': 'showInactive'
            },
            {
                'name': 'humanReadable'
            },
            {
                'name': 'includeHumanReadable'
            },
        ]
    },
    '/people/{id}/equities-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/training-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/variable-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{identifier}-GET': {
        'parameters': [
            {
                'name': 'identifier'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'humanReadable'
            },
            {
                'name': 'includeHumanReadable'
            },
        ]
    },
    '/people/{identifier}-POST': {
        'parameters': [
            {
                'name': 'identifier'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'humanReadable'
            },
        ]
    },
    '/employees/{identifier}/uninvite-POST': {
        'parameters': [
            {
                'name': 'identifier'
            },
        ]
    },
    '/people/search-POST': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'showInactive'
            },
            {
                'name': 'humanReadable'
            },
        ]
    },
    '/employees/{employeeId}/start-date-POST': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/employees/{identifier}/terminate-POST': {
        'parameters': [
            {
                'name': 'terminationDate'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'terminationReason'
            },
            {
                'name': 'reasonType'
            },
            {
                'name': 'noticePeriod'
            },
            {
                'name': 'lastDayOfWork'
            },
        ]
    },
    '/people/{id}/email-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/people/{identifier}-PUT': {
        'parameters': [
            {
                'name': 'identifier'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'personal'
            },
            {
                'name': 'about'
            },
        ]
    },
    '/people/{id}/employment/{entry_id}-PUT': {
        'parameters': [
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'contract'
            },
            {
                'name': 'type'
            },
            {
                'name': 'salaryPayType'
            },
        ]
    },
    '/people/{id}/equities/{entry_id}-PUT': {
        'parameters': [
            {
                'name': 'quantity'
            },
            {
                'name': 'equityType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'vestingCommencementDate'
            },
            {
                'name': 'consentNumber'
            },
            {
                'name': 'grantDate'
            },
            {
                'name': 'optionExpiration'
            },
            {
                'name': 'exercisePrice'
            },
            {
                'name': 'vestingTerm'
            },
            {
                'name': 'grantType'
            },
            {
                'name': 'vestingSchedule'
            },
            {
                'name': 'grantNumber'
            },
            {
                'name': 'grantStatus'
            },
        ]
    },
    '/people/{id}/work/{entry_id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'title'
            },
            {
                'name': 'department'
            },
            {
                'name': 'site'
            },
            {
                'name': 'siteId'
            },
            {
                'name': 'reportsTo'
            },
            {
                'name': 'customColumns'
            },
        ]
    },
    '/avatars/{employeeId}-PUT': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/company/reports/{reportId}/download-GET': {
        'parameters': [
            {
                'name': 'reportId'
            },
            {
                'name': 'format'
            },
            {
                'name': 'includeInfo'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'humanReadable'
            },
        ]
    },
    '/company/reports/download/{reportName}-GET': {
        'parameters': [
            {
                'name': 'reportName'
            },
        ]
    },
    '/company/reports/{reportId}/download-async-GET': {
        'parameters': [
            {
                'name': 'reportId'
            },
            {
                'name': 'format'
            },
            {
                'name': 'includeInfo'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'humanReadable'
            },
        ]
    },
    '/company/reports-GET': {
        'parameters': [
        ]
    },
    '/people/{id}/employment-POST': {
        'parameters': [
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'contract'
            },
            {
                'name': 'type'
            },
            {
                'name': 'salaryPayType'
            },
        ]
    },
    '/people/{id}/equities-POST': {
        'parameters': [
            {
                'name': 'quantity'
            },
            {
                'name': 'equityType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'vestingCommencementDate'
            },
            {
                'name': 'consentNumber'
            },
            {
                'name': 'grantDate'
            },
            {
                'name': 'optionExpiration'
            },
            {
                'name': 'exercisePrice'
            },
            {
                'name': 'vestingTerm'
            },
            {
                'name': 'grantType'
            },
            {
                'name': 'vestingSchedule'
            },
            {
                'name': 'grantNumber'
            },
            {
                'name': 'grantStatus'
            },
        ]
    },
    '/people/{id}/salaries-POST': {
        'parameters': [
            {
                'name': 'base'
            },
            {
                'name': 'payPeriod'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'payFrequency'
            },
        ]
    },
    '/people/{id}/training-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'cost'
            },
            {
                'name': 'status'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'documentId'
            },
        ]
    },
    '/people/{id}/variable-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'paymentPeriod'
            },
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'variableType'
            },
            {
                'name': 'companyPercent'
            },
            {
                'name': 'departmentPercent'
            },
            {
                'name': 'individualPercent'
            },
        ]
    },
    '/people/{id}/work-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'title'
            },
            {
                'name': 'department'
            },
            {
                'name': 'site'
            },
            {
                'name': 'siteId'
            },
            {
                'name': 'reportsTo'
            },
            {
                'name': 'customColumns'
            },
        ]
    },
    '/people/{id}/employment/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/equities/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/salaries/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/variable/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/training/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/work/{entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
        ]
    },
    '/people/{id}/employment-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/salaries-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/work-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/lifecycle-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/equities-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/training-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/variable-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/people/{id}/employment/{entry_id}-PUT': {
        'parameters': [
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'contract'
            },
            {
                'name': 'type'
            },
            {
                'name': 'salaryPayType'
            },
        ]
    },
    '/people/{id}/equities/{entry_id}-PUT': {
        'parameters': [
            {
                'name': 'quantity'
            },
            {
                'name': 'equityType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'vestingCommencementDate'
            },
            {
                'name': 'consentNumber'
            },
            {
                'name': 'grantDate'
            },
            {
                'name': 'optionExpiration'
            },
            {
                'name': 'exercisePrice'
            },
            {
                'name': 'vestingTerm'
            },
            {
                'name': 'grantType'
            },
            {
                'name': 'vestingSchedule'
            },
            {
                'name': 'grantNumber'
            },
            {
                'name': 'grantStatus'
            },
        ]
    },
    '/people/{id}/work/{entry_id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'entry_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'title'
            },
            {
                'name': 'department'
            },
            {
                'name': 'site'
            },
            {
                'name': 'siteId'
            },
            {
                'name': 'reportsTo'
            },
            {
                'name': 'customColumns'
            },
        ]
    },
    '/tasks/{taskId}/complete-POST': {
        'parameters': [
            {
                'name': 'taskId'
            },
        ]
    },
    '/my/tasks-GET': {
        'parameters': [
        ]
    },
    '/tasks-GET': {
        'parameters': [
        ]
    },
    '/tasks/people/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'task_status'
            },
        ]
    },
    '/timeoff/policy-types/{policyType}/reason-codes-POST': {
        'parameters': [
            {
                'name': 'policyType'
            },
            {
                'name': 'reasonCodes'
            },
        ]
    },
    '/timeoff/employees/{id}/requests/{requestId}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'requestId'
            },
        ]
    },
    '/timeoff/employees/{id}/adjustments-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'adjustmentType'
            },
            {
                'name': 'policyType'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/timeoff/employees/{id}/requests/{requestId}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'requestId'
            },
        ]
    },
    '/timeoff/employees/{id}/balance-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'policyType'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/timeoff/requests/changes-GET': {
        'parameters': [
            {
                'name': 'since'
            },
            {
                'name': 'includePending'
            },
        ]
    },
    '/timeoff/outtoday-GET': {
        'parameters': [
            {
                'name': 'today'
            },
            {
                'name': 'includeHourly'
            },
            {
                'name': 'includePrivate'
            },
            {
                'name': 'siteId'
            },
        ]
    },
    '/timeoff/policy-types/{policyType}-GET': {
        'parameters': [
            {
                'name': 'policyType'
            },
        ]
    },
    '/timeoff/policies-GET': {
        'parameters': [
            {
                'name': 'policyName'
            },
        ]
    },
    '/timeoff/whosout-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'includeHourly'
            },
            {
                'name': 'includePrivate'
            },
            {
                'name': 'includePending'
            },
        ]
    },
    '/timeoff/policies/names-GET': {
        'parameters': [
            {
                'name': 'policyTypeName'
            },
        ]
    },
    '/timeoff/policy-types-GET': {
        'parameters': [
        ]
    },
    '/timeoff/policy-types/{policyType}/reason-codes-GET': {
        'parameters': [
            {
                'name': 'policyType'
            },
        ]
    },
    '/timeoff/employees/{id}/requests-POST': {
        'parameters': [
            {
                'name': 'policyType'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'requestRangeType'
            },
            {
                'name': 'startDatePortion'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'minutes'
            },
            {
                'name': 'endDatePortion'
            },
            {
                'name': 'dayPortion'
            },
            {
                'name': 'dailyHours'
            },
            {
                'name': 'dailyMinutes'
            },
            {
                'name': 'skipManagerApproval'
            },
            {
                'name': 'approver'
            },
            {
                'name': 'reasonCode'
            },
        ]
    },
    '/timeoff/employees/{id}/diffHours/requests-POST': {
        'parameters': [
            {
                'name': 'policyType'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'durations'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'skipManagerApproval'
            },
            {
                'name': 'approver'
            },
            {
                'name': 'reasonCode'
            },
        ]
    },
};