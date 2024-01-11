import allure
import requests
import jsonschema
from qa_guru_diploma_api.utils.load_schema import load_schema
from qa_guru_diploma_api.utils.help_functions import get_token, get_id, get_id_to_delete


def test_get_booking(default_url):
    id = get_id()
    headers = {'Accept': 'application/json'}
    with allure.step('Отправить GET запрос на эндпоинт "/booking/{id}"'):
        result = requests.get(f'{default_url}booking/{id}',
                          headers=headers)
    schema = load_schema('get_booking.json')

    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200
    with allure.step('Проверить json схему ответа'):
        jsonschema.validate(result.json(), schema)


def test_ping_healthcheck_status_code(default_url):
    with allure.step('Отправить GET запрос на эндпоинт "/ping"'):
        result = requests.get(f'{default_url}ping')

    with allure.step('Проверить, что статус код равен 201'):
        assert result.status_code == 201


def test_create_booking(default_url):
    headers = {'Content-Type': 'application/json'}
    booking = {
        "firstname": "Jhon",
        "lastname": "Black",
        "totalprice": 111000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with allure.step('Отправить POST запрос на эндпоинт "/booking"'):
        result = requests.post(f'{default_url}booking', json=booking, headers=headers)
    schema = load_schema('create_booking.json')

    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200
    with allure.step('Проверить json схему ответа'):
        jsonschema.validate(result.json(), schema)


def test_delete_booking(default_url):
    token_func = get_token()
    token = f'token={token_func}'
    headers = {'Content-Type': 'application/json',
               'Cookie': token}
    id = get_id_to_delete()
    with allure.step('Отправить DELETE запрос на эндпоинт "/booking/{id}"'):
        result = requests.delete(f'{default_url}booking/{id}', headers=headers)

    with allure.step('Проверить, что статус код равен 201'):
        assert result.status_code == 201


def test_update_booking(default_url):
    token_func = get_token()
    token = f'token={token_func}'
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Cookie': token}
    id = get_id()
    booking = {
        "firstname": "Jhon",
        "lastname": "White",
        "totalprice": 111000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with allure.step('Отправить PUT запрос на эндпоинт "/booking/{id}"'):
        result = requests.put(f'{default_url}booking/{id}', json=booking, headers=headers)

    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200
    with allure.step('Проверить, что значение параметра lastname в ответе равно "White"'):
        assert result.json()['lastname'] == 'White'
