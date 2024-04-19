import pytest
from django.test import Client
from pytest_djangoapp import configure_djangoapp_plugin


pytest_plugins = configure_djangoapp_plugin(settings='marriage.settings')


@pytest.fixture
def client():
    return Client()
