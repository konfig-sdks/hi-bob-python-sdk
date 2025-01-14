# coding: utf-8

# flake8: noqa

"""
    Bob API

    Access your employees data with the Bob API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

__version__ = "1.0.0"

# import ApiClient
from hi_bob_python_sdk.api_client import ApiClient

# import Configuration
from hi_bob_python_sdk.configuration import Configuration

# import exceptions
from hi_bob_python_sdk.exceptions import OpenApiException
from hi_bob_python_sdk.exceptions import ApiAttributeError
from hi_bob_python_sdk.exceptions import ApiTypeError
from hi_bob_python_sdk.exceptions import ApiValueError
from hi_bob_python_sdk.exceptions import ApiKeyError
from hi_bob_python_sdk.exceptions import ApiException

from hi_bob_python_sdk.client import HiBob
