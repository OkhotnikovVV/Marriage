import pytest
from django.test import Client


def test_index_200(client: Client):
    response = client.get('')
    assert response.status_code == 200

def test_about_200(client: Client):
    response = client.get('/about/')
    assert response.status_code == 200

test_data_index_content = [
    'age_from',
    'age_to',
    'salary_from',
    'salary_to',
    'gender',
    'city',
    'marital_status',
    'education',
]

@pytest.mark.parametrize("a", test_data_index_content)
def test_index_content(client: Client, a):
    response = client.get('/about/')
    assert a in response.content.decode()

