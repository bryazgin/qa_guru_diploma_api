import requests
import jsonschema
from qa_guru_diploma_api.utils.load_schema import load_schema
from qa_guru_diploma_api.utils.help_functions import get_token, get_id, get_id_to_delete


def test_get_booking(default_url):
    id = get_id()
    headers = {'Accept': 'application/json'}
    result = requests.get(f'{default_url}booking/{id}',
                          headers=headers)
    schema = load_schema('get_booking.json')

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_ping_healthcheck_status_code(default_url):
    result = requests.get(f'{default_url}ping')

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
    result = requests.post(f'{default_url}booking', json=booking, headers=headers)
    schema = load_schema('create_booking.json')

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_delete_booking(default_url):
    token_func = get_token()
    token = f'token={token_func}'
    headers = {'Content-Type': 'application/json',
               'Cookie': token}
    id = get_id_to_delete()
    result = requests.delete(f'{default_url}booking/{id}', headers=headers)

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
    result = requests.put(f'{default_url}booking/{id}', json=booking, headers=headers)

    assert result.status_code == 200
    assert result.json()['lastname'] == 'White'
