import allure
import jsonschema
from allure_commons.types import Severity
from qa_guru_diploma_api.utils.load_schema import load_schema
from qa_guru_diploma_api.utils.help_functions import (get_token, create_booking, put_request,
                                                      get_request_with_json_response, get_request_without_json_response,
                                                      post_request, delete_request)


@allure.tag("Diploma")
@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_create_booking(default_url):
    schema = load_schema('create_booking.json')
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
        result = post_request('/booking', json=booking, headers=headers)
    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200
    with allure.step('Проверить json схему ответа'):
        jsonschema.validate(result.json(), schema)
    with allure.step(f'Проверить, что значение параметра totalprice в ответе равно 111000'):
        assert result.json()['booking']['totalprice'] == 111000


@allure.tag("Diploma")
@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_get_booking(default_url):
    id = create_booking()
    schema = load_schema('get_booking.json')
    headers = {'Accept': 'application/json'}

    with allure.step(f'Отправить GET запрос на эндпоинт "/booking/{id}"'):
        result = get_request_with_json_response(f'/booking/{id}', headers=headers)
    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200
    with allure.step('Проверить json схему ответа'):
        jsonschema.validate(result.json(), schema)
    with allure.step(f'Проверить, что значение параметра bookingid в ответе равно {id}'):
        assert result.json()['firstname'] == 'Tom'


@allure.tag("Diploma")
@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_ping_healthcheck_status_code(default_url):
    with allure.step('Отправить GET запрос на эндпоинт "/ping"'):
        result = get_request_without_json_response('/ping')
    with allure.step('Проверить, что статус код равен 201'):
        assert result.status_code == 201


@allure.tag("Diploma")
@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_delete_booking(default_url):
    token_func = get_token()
    token = f'token={token_func}'
    headers = {'Content-Type': 'application/json',
               'Cookie': token}
    id = create_booking()
    with allure.step(f'Отправить DELETE запрос на эндпоинт "/booking/{id}"'):
        result = delete_request(f'/booking/{id}', headers=headers)
    with allure.step('Проверить, что статус код равен 201'):
        assert result.status_code == 201


@allure.tag("Diploma")
@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_update_booking(default_url):
    token_func = get_token()
    token = f'token={token_func}'
    schema = load_schema('update_booking.json')
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Cookie': token}
    id = create_booking()
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
    with allure.step(f'Отправить PUT запрос на эндпоинт "/booking/{id}"'):
        result = put_request(f'/booking/{id}', json=booking, headers=headers)
    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200
    with allure.step('Проверить, что значение параметра lastname в ответе равно "White"'):
        assert result.json()['lastname'] == 'White'
    with allure.step('Проверить json схему ответа'):
        jsonschema.validate(result.json(), schema)
