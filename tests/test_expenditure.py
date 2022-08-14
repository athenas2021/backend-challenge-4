import pytest
from rest_framework.test import APIClient

# TODO - Test fail cases
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
    # test response status code
    assert response.status_code == 201
    # test data
    assert data['description'] == payload['description']
    assert float(data['value']) == float(payload['value'])
    assert data['date'] == payload['date']
    assert data['category'] == payload['category']


# test update expenditure
@pytest.mark.django_db
def test_update_expenditure():

    # TODO - pass this to fixtures
    # Create a Expenditure to test
    from expenditure.models import Expenditure
    expenditure = Expenditure.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2018-12-11',
            category=2
        )
    payload = dict(
        description='descriptionTestModified',
        value=2.00,
        date='2019-11-10',
        category=3
    )

    id = expenditure.id
    response = client.put(f"/expenditure/{id}/", payload, follow=True)
    data = response.data
    data = dict(response.data)
    # assert response status code
    assert response.status_code == 200
    # assert updates
    assert data['description'] == payload['description']
    assert float(data['value']) == float(payload['value'])
    assert data['date'] == payload['date']
    assert data['category'] == payload['category']


# test delete expenditure
@pytest.mark.django_db
def test_delete_expenditure():
    # TODO - pass this to fixtures
    # Create a Expenditure to test
    from expenditure.models import Expenditure
    expenditure = Expenditure.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2018-12-11',
            category=2
        )
    response = client.delete(f"/expenditure/{expenditure.id}/", follow=True)
    # test response status code
    assert response.status_code == 204
    # test delete
    assert len(Expenditure.objects.filter(pk=expenditure.id)) == 0


# test list expenditure
@pytest.mark.django_db
def test_list_expenditure():
    # TODO - pass this fixtures
    # Create a Expenditure to test
    from expenditure.models import Expenditure
    expenditure = Expenditure.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2018-12-11',
            category=2
    )
    response = client.get("/expenditure/", follow=True)
    data = dict(response.data)
    # test response status code
    assert response.status_code == 200
    # test list count
    assert response.data['count'] == 1
    # test list fields
    assert (data['results'])[0]['id'] == expenditure.id
    assert (data['results'])[0]['description'] == expenditure.description
    assert float((data['results'])[0]['value']) == float(expenditure.value)
    assert (data['results'])[0]['date'] == expenditure.date
    assert (data['results'])[0]['category'] == expenditure.category


# test retrieve expenditure
@pytest.mark.django_db
def test_retrieve_expenditure():
    # TODO - pass this fixtures
    # Create a Expenditure to test
    from expenditure.models import Expenditure
    expenditure = Expenditure.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2018-12-11',
            category=2
    )
    response = client.get(f"/expenditure/{expenditure.id}/", follow=True)
    data = response.data
    # test response status code
    assert response.status_code == 200
    # test retrieve lenght
    assert len(data) == 5
    # test retrieve fields
    assert data['id'] == expenditure.id
    assert data['description'] == expenditure.description
    assert float(data['value']) == float(expenditure.value)
    assert data['date'] == expenditure.date
    assert data['category'] == expenditure.category


# test serch by month expenditure
@pytest.mark.django_db
def test_search_by_month_expenditure():
    # TODO - pass this fixtures
    # Create a Expenditure to test
    from expenditure.models import Expenditure
    expenditure = Expenditure.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2022-12-11',
            category=2
    )
    response = client.get("/expenditure/12/2022/", follow=True)
    data = response.data
    # test reponse status code
    assert response.status_code == 200
    # test response count lenght
    assert data['count'] == 1
    # test retrieve fields
    assert (data['results'])[0]['id'] == expenditure.id
    assert (data['results'])[0]['description'] == expenditure.description
    assert float((data['results'])[0]['value']) == float(expenditure.value)
    assert (data['results'])[0]['date'] == expenditure.date
    assert (data['results'])[0]['category'] == expenditure.category
