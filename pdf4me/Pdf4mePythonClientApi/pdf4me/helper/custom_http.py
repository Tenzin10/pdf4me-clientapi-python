import requests

from pdf4me.helper.json_converter import JsonConverter
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException, Pdf4meBackendException
from pdf4me.helper.response_checker import ResponseChecker
from pdf4me.helper.token_generator import TokenGenerator

URL = "https://api-dev.pdf4me.com/"


class CustomHttp(object):

    def __init__(self, client_id, secret):

        self.client_id = client_id
        self.secret = secret

        self.token_generator = TokenGenerator(client_id, secret)
        self.json_converter = JsonConverter()

    def post_universal_object(self, universal_object, controller):
        """Sends a post request to the specified controller with the given
        universal_object as a body.

        :param universal_object: object to be sent
        :type universal_object: object
        :param controller: swagger controller
        :type controller: str
        :return: post response
        """

        # prepare post request
        token = self.token_generator.get_token()
        request_url = URL + controller
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

        # convert body to json
        body = self.json_converter.dump(element=universal_object)

        # send request
        res = requests.post(request_url, data=body, headers=headers)

        # check status code
        self.__check_status_code(res)

        # check docLogs for error messages
        self.__check_docLogs_for_error_messages(res)

        # read content from response
        json_response = self.json_converter.load(res.text)

        return json_response

    def post_wrapper(self, octet_streams, values, controller):
        """Builds a post requests from the given parameters.

        :param octet_streams: (key: file identifier, value: open(fileName, 'rb'))) pairs
        :type octet_streams: list
        :param values: (key: identifier of value, value: content of value) pairs
        :type values: list
        :param controller: swagger controller
        :type controller: str
        :return: post response
        """

        # prepare post request
        token = self.token_generator.get_token()
        request_url = URL + controller
        header = {'Authorization': 'Bearer ' + token}

        # build files
        if len(octet_streams) != 0:
            files = {key: value for (key, value) in octet_streams}
        else:
            files = None

        # build values
        if len(values) != 0:
            data = {key: value for (key, value) in values}
        else:
            data = None

        # send request
        if files is None:
            if data is None:
                raise Pdf4meClientException("Please provide at least one value or an octet-stream.")
            else:
                res = requests.post(request_url, data=data, headers=header)
        else:
            if data is None:
                res = requests.post(request_url, files=files, headers=header)
            else:
                res = requests.post(request_url, files=files, data=data, headers=header)

        # check status code
        self.__check_status_code(res)

        # check docLogs for error messages
        self.__check_docLogs_for_error_messages(res)

        return res.content

    def __check_status_code(self, response):
        '''
        Checks whether the status code is either 200 or 204, otw. throws a Pdf4meBackendException.
        :param response: post response
        :type response: requests.Response
        :return: None
        '''

        status_code = response.status_code
        status_reason = response.reason

        if status_code == 500:
            server_error = self.json_converter.load(response.text)['error_message']
            raise Pdf4meBackendException('HTTP 500 ' + status_reason + " : " + server_error)
        elif status_code != 200 and status_code != 204:
            error = response.text
            raise Pdf4meBackendException('HTTP ' + status_code + ': ' + status_reason + " : " + error)

    def __check_docLogs_for_error_messages(self, response):
        '''
        Checks whether the HTTP response's docLogs contain any error message, in case of an error
         a Pdf4meBackendException is thrown.
        :param response: post response
        :type response: requests.Response
        :return: None
        '''

        ResponseChecker().check_response_for_errors(response.text)
