import random
import requests


def get_token():
    result = requests.post('https://restful-booker.herokuapp.com/auth', data={
        "username": "admin",
        "password": "password123"
    })
    token = result.json()['token']
    return token


def get_id():
    ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    id = random.choice(ids)
    return id


def get_id_to_delete():
    ids = [111, 222, 333, 444, 555, 666, 777, 888, 999, 101, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    id = random.choice(ids)
    return id
