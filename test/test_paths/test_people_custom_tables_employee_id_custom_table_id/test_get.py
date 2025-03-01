# coding: utf-8

"""
    Bob API

    Access your employees data with the Bob API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import hi_bob_python_sdk
from hi_bob_python_sdk.paths.people_custom_tables_employee_id_custom_table_id import get
from hi_bob_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPeopleCustomTablesEmployeeIdCustomTableId(ApiTestMixin, unittest.TestCase):
    """
    PeopleCustomTablesEmployeeIdCustomTableId unit test stubs
        Read all entries of the given custom table
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
