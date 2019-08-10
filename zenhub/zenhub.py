# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 John J. Rofrano <rofrano@gmail.com>
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
ZenHub Module
"""
import requests
from urllib.parse import urljoin
from .repository import Repository

class ZenHub:
    """
    Python binding for the ZenHub API described at https://github.com/ZenHubIO/API

    This base class provides the API endpoint and convinience methods
    to perform HTTP GET, POST, PUT, PATCH that other classes in this library
    will use to communicate to the ZenHub API.
    """

    DEFAULT_API_ENDPOINT = 'https://api.zenhub.io'

    def __init__(self, api_token, api_endpoint=DEFAULT_API_ENDPOINT):
        self.api_token = api_token
        self.api_endpoint = api_endpoint
        self.headers = {'X-Authentication-Token': self.api_token}

    def repository(self, repo_id):
        """ Returns a repository given it's ID

        :type repo_id: int
        :param repo_id: The GitHub ID of the repository

        :return: a repository object
        :rtype: :class:`github.Repo`
        """
        return Repository(repo_id, self)

    def _check_response(self, response):
        """ Private method that checks the response for valid return codes

        :type response: :class:`requests.Response`
        :param response: The response from an http request

        :return: the response as json dictionary if content was sent
        :rtype: dict

        :raise HTTPError: received something other then ``200`` or ``404``
        """
        if response.status_code == requests.codes.ok:
            # Since the ZenHub REST API does not send back 204 when there is
            # no content, we have to check the Content-Length for 0 :(
            if int(response.headers['Content-Length']):
                return response.json()
        elif response.status_code == requests.codes.not_found:
            return None
        else:
            return response.raise_for_status()

    def get(self, path):
        """ Performs an http GET for the given path

        :type path: string
        :param path: The path after the api endpoint (e.g., ``'/p1/repositories'``)

        :return: the response as json dictionary if content was found or None if it was not
        :rtype: dict or None

        :raise requests.exceptions.HTTPError: received something other then ``200`` or ``404``
        """
        url = urljoin(self.api_endpoint, path)
        response = requests.get(url, headers=self.headers)
        if response.status_code == requests.codes.ok:
            return response.json()
        elif response.status_code == requests.codes.not_found:
            return None
        else:
            response.raise_for_status()

    def post(self, path, body):
        """ Performs an http POST for the given path

        :type path: string
        :param path: The path after the api endpoint (e.g., ``'/p1/repositories'``)
        :type body: dict
        :param body: A Python `dict` containing data to be created

        :return: The response as json dictionary if content was sent
        :rtype: dict

        :raise requests.exceptions.HTTPError: received something other then ``200`` or ``404``
        """
        url = urljoin(self.api_endpoint, path)
        response = requests.post(url, json=body, headers=self.headers)
        return self._check_response(response)

    def put(self, path, body):
        """ Performs an http PUT for the given path

        :type path: string
        :param path: The path after the api endpoint (e.g., ``'/p1/repositories'``)
        :type body: dict
        :param body: A Python `dict` containing data to be updated

        :return: the response as json dictionary if content was sent
        :rtype: dict

        :raise requests.exceptions.HTTPError: received something other then ``200`` or ``404``
        """
        url = urljoin(self.api_endpoint, path)
        response = requests.put(url, json=body, headers=self.headers)
        return self._check_response(response)

    def patch(self, path, body):
        """ Performs an http PATCH for the given path

        :type path: string
        :param path: The path after the api endpoint (e.g., ``'/p1/repositories'``)
        :type body: dict
        :param body: A Python `dict` containing data to be patched

        :return: the response as json dictionary if content was sent
        :rtype: dict

        :raise requests.exceptions.HTTPError: received something other then ``200`` or ``404``
        """
        url = urljoin(self.api_endpoint, path)
        response = requests.patch(url, json=body, headers=self.headers)
        return self._check_response(response)
