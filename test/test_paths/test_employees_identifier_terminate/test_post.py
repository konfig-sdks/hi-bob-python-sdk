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
from hi_bob_python_sdk.paths.employees_identifier_terminate import post
from hi_bob_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestEmployeesIdentifierTerminate(ApiTestMixin, unittest.TestCase):
    """
    EmployeesIdentifierTerminate unit test stubs
        Terminate company employee.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
