import pytest
from rest_framework.test import APIClient

# TODO - Test fail cases
client = APIClient()

# test create revenue
@pytest.mark.django_db
def test_create_revenue():
    payload = dict(
        description='descriptionTest',
        value=1.00,
        date='2018-12-11',
    )
    response = client.post('/revenue/', payload)
    data = response.data
    # test response status code
    assert response.status_code == 201
    # test data
    assert data['description'] == payload['description']
    assert float(data['value']) == float(payload['value'])
    assert data['date'] == payload['date']


# test update revenue
@pytest.mark.django_db
def test_update_revenue():

    # TODO - pass this to fixtures
    # Create a revenue to test
    from revenue.models import Revenue
    revenue = Revenue.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2018-12-11',
        )
    payload = dict(
        description='descriptionTestModified',
        value=2.00,
        date='2019-11-10',
    )

    id = revenue.id
    response = client.put(f"/revenue/{id}/", payload, follow=True)
    data = response.data
    data = dict(response.data)
    # assert response status code
    assert response.status_code == 200
    # assert updates
    assert data['description'] == payload['description']
    assert float(data['value']) == float(payload['value'])
    assert data['date'] == payload['date']


# test delete revenue
@pytest.mark.django_db
def test_delete_revenue():
    # TODO - pass this to fixtures
    # Create a revenue to test
    from revenue.models import Revenue
    revenue = Revenue.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2018-12-11',
        )
    response = client.delete(f"/revenue/{revenue.id}/", follow=True)
    # test response status code
    assert response.status_code == 204
    # test delete
    assert len(Revenue.objects.filter(pk=revenue.id)) == 0


# test list revenue
@pytest.mark.django_db
def test_list_revenue():
    # TODO - pass this fixtures
    # Create a revenue to test
    from revenue.models import Revenue
    revenue = Revenue.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2018-12-11',
    )
    response = client.get("/revenue/", follow=True)
    data = dict(response.data)
    # test response status code
    assert response.status_code == 200
    # test list count
    assert response.data['count'] == 1
    # test list fields
    assert (data['results'])[0]['id'] == revenue.id
    assert (data['results'])[0]['description'] == revenue.description
    assert float((data['results'])[0]['value']) == float(revenue.value)
    assert (data['results'])[0]['date'] == revenue.date


# test retrieve revenue
@pytest.mark.django_db
def test_retrieve_revenue():
    # TODO - pass this fixtures
    # Create a revenue to test
    from revenue.models import Revenue
    revenue = Revenue.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2018-12-11',
    )
    response = client.get(f"/revenue/{revenue.id}/", follow=True)
    data = response.data
    # test response status code
    assert response.status_code == 200
    # test retrieve lenght
    assert len(data) == 5
    # test retrieve fields
    assert data['id'] == revenue.id
    assert data['description'] == revenue.description
    assert float(data['value']) == float(revenue.value)
    assert data['date'] == revenue.date


# test serch by month revenue
@pytest.mark.django_db
def test_search_by_month_revenue():
    # TODO - pass this fixtures
    # Create a revenue to test
    from revenue.models import Revenue
    revenue = Revenue.objects.create(
            description='descriptionTest',
            value=1.00,
            date='2022-12-11',
    )
    response = client.get("/revenue/12/2022/", follow=True)
    data = response.data
    # test reponse status code
    assert response.status_code == 200
    # test response count lenght
    assert data['count'] == 1
    # test retrieve fields
    assert (data['results'])[0]['id'] == revenue.id
    assert (data['results'])[0]['description'] == revenue.description
    assert float((data['results'])[0]['value']) == float(revenue.value)
    assert (data['results'])[0]['date'] == revenue.date
    assert (data['results'])[0]['category'] == revenue.category
