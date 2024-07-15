import requests
import allure
import pytest

BASE_URL = 'https://reqres.in/'


@allure.feature('User Registration and Login')
@allure.suite('Registration Tests')
@allure.title('Test Negative Register User')
@pytest.mark.regression
class TestRegistration:

    def test_negative_register_user(self):
        data = {
             "email": "sydney@fife"
        }
        response = requests.post(f'{BASE_URL}/api/register', json=data)
        response_data = response.json()
        with allure.step('Check status code'):
            assert response.status_code == 400, f'Status Code should be 400, but got {response.status_code}'
        with allure.step('Check for error in response'):
            assert 'error' in response_data, "'error' is empty"
        with allure.step('Verify error message'):
            assert response_data['error'] == "Missing password", f"error message should be 'Missing password', but got {response_data['error']}"

    @allure.suite('Registration Tests')
    @allure.title('Test Register User')
    @pytest.mark.regression
    def test_register_user(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = requests.post(f'{BASE_URL}/api/register', json=data)
        response_data = response.json()
        with allure.step('Check status code'):
            assert response.status_code == 200, f'Status Code should be 200, but got {response.status_code}'
        with allure.step('Check for id in response'):
            assert 'id' in response_data, "'id' is missing"
        with allure.step('check id is not empty '):
            assert response_data['id'] != '', "'id' is empty"
        with allure.step('Check for token in response'):
            assert 'token' in response_data, "'token' is missing"
        with allure.step('check token is not empty '):
            assert response_data['token'] != '', "'token' is empty"

    @allure.suite('Login Tests')
    @allure.title('Test Negative Login User')
    @pytest.mark.regression
    def test_negative_login_user(self):
        data = {
             "email": "peter@klaven"
        }
        response = requests.post(f'{BASE_URL}/api/login', json=data)
        response_data = response.json()
        with allure.step('Check status code'):
            assert response.status_code == 400, f'Status Code should be 400, but got {response.status_code}'
        with allure.step('Check for error in response'):
            assert 'error' in response_data, "'error' is empty"
        with allure.step('Verify error message'):
            assert response_data['error'] == "Missing password", f"error message should be 'Missing password', but got {response_data['error']}"

    @allure.suite('Login Tests')
    @allure.title('Test Login User')
    @pytest.mark.regression
    def test_login_user(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = requests.post(f'{BASE_URL}/api/login', json=data)
        response_data = response.json()
        with allure.step('Check status code'):
            assert response.status_code == 200, f'Status Code should be 200, but got {response.status_code}'
        with allure.step('Check for token in response'):
            assert 'token' in response_data, "'token' is missing"
        with allure.step('check token is not empty '):
            assert response_data['token'] != '', "'token' is empty"

