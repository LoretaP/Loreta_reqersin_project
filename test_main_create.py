import requests
import allure
import pytest

BASE_URL = 'https://reqres.in/'

class TestCUPD:
    @pytest.fixture()
    def create_user(self):
        data = {
            "name": "morpheus",
            "job": "leader"
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(
            f'{BASE_URL}/api/users',
            json=data,
            headers=headers
        )
        new_id = response.json()['id']

        yield new_id


    @allure.feature('User Management')
    @allure.suite('User Creation')
    @allure.title('Test Create User')
    @allure.description('Verify that a user can be created with a valid name and job')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_create_user(self):
        data = {
            "name": "Loreta",
            "job": "leader"
        }
        response = requests.post(
            f'{BASE_URL}/api/users',
            json=data
        )

        response_data = response.json()
        with allure.step('Check response status code is 201'):
            assert response.status_code == 201, f'Status Code should be 201, but got {response.status_code}'
        with allure.step('Check response name is "Loreta"'):
            assert response_data["name"] == "Loreta"
        with allure.step('Check response job is "leader"'):
            assert response_data["job"] == "leader"


    @allure.feature('User Management')
    @allure.suite('User Update')
    @allure.title('Test Update User')
    @allure.description('Verify that a user can be updated with a new name and job')
    @pytest.mark.regression
    @pytest.mark.smoke

    def test_update_user(self,create_user):
        new_id = create_user
        data = {
            "name": "Loreta Petrosyan",
            "job": "zion resident"
        }
        response = requests.put(
            f'{BASE_URL}/api/users/{new_id}',
            json=data
        )

        response_data = response.json()
        with allure.step('Check response status code is 200'):
            assert response.status_code == 200, f'Status Code should be 200, but got {response.status_code}'
        with allure.step('Check updated name is "Loreta Petrosyan"'):
            assert response_data["name"] == "Loreta Petrosyan"
        with allure.step('Check updated job is "zion resident"'):
            assert response_data["job"] == "zion resident"


    @allure.feature('User Management')
    @allure.suite('User Partial Update')
    @allure.title('Test Partial Update User')
    @allure.description('Verify that a user can be partially updated with a new name and job')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_partial_update_user(self,create_user):
        new_id = create_user
        data = {
            "name": "Petrosyan Loreta",
            "job": "zion resident"
        }
        response = requests.patch(
            f'{BASE_URL}/api/users/{new_id}',
            json=data
        )

        response_data = response.json()
        with allure.step('Check response status code is 200'):
            assert response.status_code == 200, f'Status Code should be 200, but got {response.status_code}'
        with allure.step('Check partially updated name is "Petrosyan Loreta"'):
            assert response_data["name"] == "Petrosyan Loreta"
        with allure.step('Check partially updated job is "zion resident"'):
            assert response_data["job"] == "zion resident"


    @allure.feature('User Management')
    @allure.suite('User Deletion')
    @allure.title('Test Delete User')
    @allure.description('Verify that a user can be deleted')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_delete_user(self,create_user):
        new_id = create_user
        response = requests.delete(f'{BASE_URL}/api/users/{new_id}')
        with allure.step('Check response status code is 204'):
            assert response.status_code == 204, f'Status Code should be 204, but got {response.status_code}'
