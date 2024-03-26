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
from hi_bob_python_sdk.paths.docs_people_id_confidential_doc_id import delete
from hi_bob_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDocsPeopleIdConfidentialDocId(ApiTestMixin, unittest.TestCase):
    """
    DocsPeopleIdConfidentialDocId unit test stubs
        Delete a specific document from the employee's confidential folder.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200


if __name__ == '__main__':
    unittest.main()
