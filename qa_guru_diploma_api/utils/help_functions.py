import logging
import requests


def get_token():
    result = requests.post('https://restful-booker.herokuapp.com/auth', data={
        "username": "admin",
        "password": "password123"
    })
    token = result.json()['token']
    return token


def console_logging(result):
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)


def create_booking():
    headers = {'Content-Type': 'application/json'}
    booking = {
        "firstname": "Tom",
        "lastname": "Soyer",
        "totalprice": 111222,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    result = requests.post('https://restful-booker.herokuapp.com/booking', json=booking, headers=headers)
    result_id = result.json()['bookingid']
    return result_id
