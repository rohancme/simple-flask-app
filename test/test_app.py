from src.app import get_resp_dict
from src.app import app
import pytest


def get_giphy_string():
    return "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="


def test_giphy_response():
    url = get_giphy_string()
    resp = get_resp_dict(url)
    if resp is None:
        pytest.fail("Unable to get data from giphy")


def test_response_obj():
    resp = app.test_client().get('/')
    assert(resp.status_code == 200)
