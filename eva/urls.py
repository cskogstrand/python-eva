"""
Eva urls.
"""

# pylint: disable=missing-docstring

BASE_URLS = [
    'https://home-hla.smarthome-test.datek.io',
    'https://home-hla.smarthome-qa.datek.io',
    'https://home-hla.evasmart.no',
]
BASE_URL = None


def get_homes():
    return '{base_url}/homes'.format(
        base_url=BASE_URL)


def get_home(home_id):
    return '{base_url}/homes/{home_id}'.format(
        base_url=BASE_URL,
        home_id=home_id)
