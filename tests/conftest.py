import pytest
from selene import browser


@pytest.fixture
def url_config():
    browser.config.base_url = 'https://restful-booker.herokuapp.com/'
