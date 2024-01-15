import json
import logging
import allure
import requests
from allure_commons.types import AttachmentType


def get_token():
    result = requests.post('https://restful-booker.herokuapp.com/auth', data={
        "username": "admin",
        "password": "password123"
    })
    token = result.json()['token']
    return token


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


def get_request_with_json_response(url, **kwargs):
    result = requests.get(url='https://restful-booker.herokuapp.com' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response body",
                  attachment_type=AttachmentType.JSON, extension="json")
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result


def get_request_without_json_response(url, **kwargs):
    result = requests.get(url='https://restful-booker.herokuapp.com' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result


def delete_request(url, **kwargs):
    result = requests.delete(url='https://restful-booker.herokuapp.com' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result


def post_request(url, **kwargs):
    result = requests.post(url='https://restful-booker.herokuapp.com' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.body, name="Request body", attachment_type=AttachmentType.JSON,
                  extension="json")
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response body",
                  attachment_type=AttachmentType.JSON, extension="json")
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result


def put_request(url, **kwargs):
    result = requests.put(url='https://restful-booker.herokuapp.com' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.body, name="Request body", attachment_type=AttachmentType.JSON,
                  extension="json")
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response body",
                  attachment_type=AttachmentType.JSON, extension="json")
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result
