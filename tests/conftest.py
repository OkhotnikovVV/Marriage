from pytest_djangoapp import configure_djangoapp_plugin

pytest_plugins = configure_djangoapp_plugin(settings='marriage.settings')

import pytest
from django.test import Client

@pytest.fixture
def client():
    return Client()
