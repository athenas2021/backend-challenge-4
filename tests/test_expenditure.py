import pytest
from rest_framework.test import APIClient
from datetime import date


client = APIClient()
# test create expenditure
@pytest.mark.django_db
def test_create_expenditure():
    payload = dict(
        description='descriptionTest',
        value=1.00,
        date='2018-12-11',
        category=2
    )
    response = client.post('/expenditure/', payload)
    data = response.data
    assert response.status_code == 201
    assert data['description'] == payload['description']
    assert float(data['value']) == float(payload['value'])
    assert data['date'] == payload['date']
    assert data['category'] == payload['category']


# test update expenditure
# test delete expenditure
# test list expenditure
# test retrieve expenditure
# test serch by month expenditure
