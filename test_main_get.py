import requests
import allure
import pytest

BASE_URL = 'https://reqres.in/'


class TestGets:

    @allure.feature('User API')
    @allure.suite('Negative Tests')
    @allure.title('Test Non-Existent Single User')
    @pytest.mark.regression
    def test_negative_single_user(self):

        response = requests.get(f'{BASE_URL}/api/users/23')
        with allure.step('Verify status code is 404'):
            assert response.status_code == 404, f'Status Code should be 404, but got {response.status_code}'

    @allure.feature('User API')
    @allure.suite('Single User')
    @allure.title('Test Single User')
    @pytest.mark.regression
    def test_single_user(self):
        response = requests.get(f'{BASE_URL}/api/users/2')
        response_data = response.json()

        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, f'Status Code should be 200, but got {response.status_code}'

        with allure.step('Verify data field exists'):
            assert 'data' in response_data, "'data' not found"

        data = response_data['data']  # Accessing 'data' field

        with allure.step('Verify Id is not empty'):
            assert data['id'] != '', 'id is missing'

        with allure.step('Verify email is not empty'):
            assert data['email'] != '', 'email is missing'

        with allure.step('Verify last_name is not empty'):
            assert data['last_name'] != '', 'last_name is missing'


    @allure.feature('User API')
    @allure.suite('User Listing')
    @allure.title('Test List Users')
    @pytest.mark.regression
    def test_list_users(self):
        response = requests.get(f'{BASE_URL}/api/users?page=2')
        response_data = response.json()
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, f'Status Code should be 200, but got {response.status_code}'
        with allure.step('Verify page number'):
            assert 'page' in response_data, "'page' not found"
            assert 'per_page' in response_data, "'per_page' not found"
            assert response_data['per_page'] == 6, f"'per_page' should be 6, but got {response_data['per_page']}"
        with allure.step('Verify total value'):
            assert 'total' in response_data, "'total' not found"
            assert response_data['total'] == 12, f"'total' should be 12, but got {response_data['total']}"
        with allure.step('Verify total_pages value'):
            assert 'total_pages' in response_data, "'total_pages' not found"
            assert response_data['total_pages'] == 2, f"'total_pages' should be 2, but got {response_data['total_pages']}"
        with allure.step('Verify data field'):
            assert 'data' in response_data, "'data' not found"
            assert len(response_data['data']) > 0, "'data' should not be empty"

    @allure.feature('Unknown API')
    @allure.suite('Resource Retrieval')
    @allure.title('Negative Test: Non-existent Resource')
    @pytest.mark.regression
    def test_negative_resource(self):

        response = requests.get(f'{BASE_URL}/api/unknown/23')
        with allure.step('Verify status code is 404'):
            assert response.status_code == 404, f'Status Code should be 404, but got {response.status_code}'

    @allure.feature('Unknown API')
    @allure.suite('Single Resource Retrieval')
    @allure.title('Positive Test: Single Resource')
    @pytest.mark.regression
    def test_single_source(self):
        response = requests.get(f'{BASE_URL}/api/unknown/2')
        response_data = response.json()

        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, f'Status Code should be 200, but got {response.status_code}'

        with allure.step('Verify data field exists'):
            assert 'data' in response_data, "'data' not found"

        with allure.step('Verify support field exists'):
            assert 'support' in response_data, "'support' not found"

        with allure.step('Verify Id is not empty'):
            assert response_data['data']['id'] != '', 'id is missing'

        with allure.step('Verify name is not empty'):
            assert response_data['data']['name'] != '', 'name is missing'

        with allure.step('Verify year is not empty'):
            assert response_data['data']['year'] != '', 'year is missing'

        with allure.step('Verify color is not empty'):
            assert response_data['data']['color'] != '', 'color is missing'

        with allure.step('Verify pantone_value is not empty'):
            assert response_data['data']['pantone_value'] != '', 'pantone_value is missing'

        with allure.step('Verify support url is not empty'):
            assert response_data['support']['url'] != '', 'support url is missing'

        with allure.step('Verify support text is not empty'):
            assert response_data['support']['text'] != '', 'support text is missing'

    @allure.feature('Unknown API')
    @allure.suite('List of Resources')
    @allure.title('Positive Test: List Users')
    @pytest.mark.regression
    def test_list_users(self):
        response = requests.get(f'{BASE_URL}/api/unknown')
        response_data = response.json()
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, f'Status Code should be 200, but got {response.status_code}'
        with allure.step('Verify page number'):
            assert 'page' in response_data, "'page' not found"
            assert 'per_page' in response_data, "'per_page' not found"
            assert response_data['per_page'] == 6, f"'per_page' should be 6, but got {response_data['per_page']}"
        with allure.step('Verify total value'):
            assert 'total' in response_data, "'total' not found"
            assert response_data['total'] == 12, f"'total' should be 12, but got {response_data['total']}"
        with allure.step('Verify total_pages value'):
            assert 'total_pages' in response_data, "'total_pages' not found"
            assert response_data['total_pages'] == 2, f"'total_pages' should be 2, but got {response_data['total_pages']}"
        with allure.step('Verify data field'):
            assert 'data' in response_data, "'data' not found"
            assert len(response_data['data']) > 0, "'data' should not be empty"
        for resource in response_data['data']:
            with allure.step(f"Verify resource {resource['id']} details"):
                assert 'id' in resource and resource['id'] != '', 'id is missing'
                assert 'name' in resource and resource['name'] != '', 'name is missing'
                assert 'year' in resource and resource['year'] != '', 'year is missing'
                assert 'color' in resource and resource['color'] != '', 'color is missing'
                assert 'pantone_value' in resource and resource['pantone_value'] != '', 'pantone_value is missing'

    @allure.feature('Users API')
    @allure.suite('List Users')
    @allure.title('Positive Test: List Users with Delay')
    @pytest.mark.regression
    def test_list_users_with_delay(self):
        with allure.step(f" {BASE_URL}/api/users?delay=3"):
            response = requests.get(f'{BASE_URL}/api/users?delay=3')
            response_data = response.json()

        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, f'Status Code should be 200, but got {response.status_code}'

        with allure.step('Verify page number'):
            assert 'page' in response_data, "'page' not found"
            assert 'per_page' in response_data, "'per_page' not found"
            assert response_data['per_page'] == 6, f"'per_page' should be 6, but got {response_data['per_page']}"

        with allure.step('Verify total value'):
            assert 'total' in response_data, "'total' not found"
            assert response_data['total'] == 12, f"'total' should be 12, but got {response_data['total']}"

        with allure.step('Verify total_pages value'):
            assert 'total_pages' in response_data, "'total_pages' not found"
            assert response_data['total_pages'] == 2, f"'total_pages' should be 2, but got {response_data['total_pages']}"

        with allure.step('Verify data field'):
            assert 'data' in response_data, "'data' not found"
            assert len(response_data['data']) > 0, "'data' should not be empty"

