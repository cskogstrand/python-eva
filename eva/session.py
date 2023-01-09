'''
Eva session, using Eva app api
'''

import json
import requests
from . import urls
import os


def _validate_response(response):
    """ Verify that response is OK """
    if response.status_code == 200:
        return
    raise ResponseError(response.status_code, response.text)


class Error(Exception):
    ''' Eva session error '''
    pass


class RequestError(Error):
    ''' Wrapped requests.exceptions.RequestException '''
    pass


class LoginError(Error):
    ''' Login failed '''
    pass


class ResponseError(Error):
    ''' Unexcpected response '''

    def __init__(self, status_code, text):
        super(ResponseError, self).__init__(
            'Invalid response'
            ', status code: {0} - Data: {1}'.format(
                status_code,
                text))
        self.status_code = status_code
        self.text = text


class Session(object):
    """ Eva app session

    Args:
        username (str): Username used to login to Eva app
        password (str): Password used to login to Eva app

    """

    def __init__(self, username, password, environment, home_id,
                 cookieFileName='~/.eva-cookie'):
        self._username = username
        self._password = password
        self._environment = environment
        self._cookieFileName = os.path.expanduser(cookieFileName)
        self._request_headers = {
            'APPLICATION_ID': 'PS_PYTHON',
            'Accept': 'application/json',
            'Content-Type': 'application/json'}
        self._request_cookies = None
        self.homes = None  # self._get_homes()
        self.home = None  # self._get_home(home_id)

    @property
    def get_base_url(self):
        env = self._environment
        match env.lower():
            case 'test':
                return urls.BASE_URLS[0]
            case 'qa':
                return urls.BASE_URLS[1]
            case default:
                return urls.BASE_URLS[2]

    def _get_homes(self):
        """ Get homes for chosen environment """
        response = None
        base_url = self.get_base_url  # urls.BASE_URLS[1]
        urls.BASE_URL = base_url
        print(base_url)
        try:
            response = requests.get(
                urls.get_homes(),
                headers=self._request_headers,
                cookies=self._request_cookies,
                auth=(self._username, self._password)
            )
            if 200 != response.status_code:
                raise ResponseError(response.status_code, response.text)
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)

        _validate_response(response)
        #         self.homes =
        return json.loads(response.text)["homes"]

    def _get_home(self, home_id):
        """ Get homes for chosen environment """
        response = None
        #         for base_url in urls.BASE_URLS:
        base_url = urls.BASE_URLS[1]
        urls.BASE_URL = base_url
        print(base_url)
        try:
            response = requests.get(
                urls.get_home(home_id),
                headers=self._request_headers,
                cookies=self._request_cookies,
                auth=(self._username, self._password)
            )
            if 200 != response.status_code:
                raise ResponseError(response.status_code, response.text)
        except requests.exceptions.RequestException as ex:
            raise RequestError(ex)

        _validate_response(response)
        #         self.homes =
        return json.loads(response.text)
