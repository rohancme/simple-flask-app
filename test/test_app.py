from source.app import get_resp_dict
import pytest


def get_giphy_string():
    return "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="


def test_good_response():
    url = get_giphy_string()
    resp = get_resp_dict(url)
    if resp is None:
        pytest.fail("Unable to get data from giphy")
