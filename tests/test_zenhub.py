"""
Test cases for ZenHub class
"""
import json
import logging
from unittest import TestCase, mock
from requests import Response
from requests.exceptions import HTTPError
from zenhub import ZenHub, Repository

######################################################################
#  T E S T   C A S E S
######################################################################
class TestZenHub(TestCase):
    """ Test Cases for ZenHub class """

    def test_contructor(self):
        """ Create / Constructor """
        zen = ZenHub('ZENHUB_TOKEN')
        self.assertEqual(zen.api_token, 'ZENHUB_TOKEN')
        self.assertEqual(zen.api_endpoint, ZenHub.DEFAULT_API_ENDPOINT)
        self.assertEqual(zen.headers, {'X-Authentication-Token': 'ZENHUB_TOKEN'})

    def test_repository(self):
        """ Test Get repository """
        zen = ZenHub('ZENHUB_TOKEN')
        repo = zen.repository(12345)
        self.assertIsInstance(repo, Repository)
        self.assertEqual(repo.id, 12345)
        self.assertEqual(repo.zenhub, zen)

    @mock.patch('requests.get')
    def test_get_request(self, mock_request):
        """ Test GET Request """
        mock_request.return_value = mock.MagicMock(spec=Response,
                                                   status_code=200)
        mock_request.return_value.json.return_value = {"message":"ok!"}
        zen = ZenHub('ZENHUB_TOKEN')
        resp = zen.get('/phony')
        logging.error(resp)
        self.assertEqual(resp['message'], 'ok!')

    @mock.patch('requests.get')
    def test_get_request_not_found(self, mock_request):
        """ Test GET Not Found """
        mock_request.return_value = mock.MagicMock(spec=Response,
                                                   status_code=404)
        zen = ZenHub('ZENHUB_TOKEN')
        resp = zen.get('/phony')
        logging.error(resp)
        self.assertIsNone(resp)

    @mock.patch('requests.get')
    def test_get_not_auth(self, mock_request):
        """ Test GET Not Authorized """
        mock_request.return_value = mock.MagicMock(spec=Response,
                                                   status_code=401)
        mock_request.return_value.raise_for_status.side_effect = HTTPError(401)

        zen = ZenHub('ZENHUB_TOKEN')
        self.assertRaises(HTTPError, zen.get, '/phony')

    @mock.patch('requests.post')
    def test_post_request(self, mock_request):
        """ Test POST Request """
        headers = {
            "Content-Length": 17
        }
        mock_request.return_value = mock.MagicMock(spec=Response,
                                                   status_code=200,
                                                   headers=headers)
        mock_request.return_value.json.return_value = {"message":"ok!"}
        zen = ZenHub('ZENHUB_TOKEN')
        resp = zen.post('/phony', {"message":"ok!"})
        logging.error(resp)
        self.assertEqual(resp['message'], 'ok!')

    @mock.patch('requests.put')
    def test_put_request(self, mock_request):
        """ Test PUT Request """
        headers = {
            "Content-Length": 17
        }
        mock_request.return_value = mock.MagicMock(spec=Response,
                                                   status_code=200,
                                                   headers=headers)
        mock_request.return_value.json.return_value = {"message":"ok!"}
        zen = ZenHub('ZENHUB_TOKEN')
        resp = zen.put('/phony', {"message":"ok!"})
        logging.error(resp)
        self.assertEqual(resp['message'], 'ok!')

    @mock.patch('requests.put')
    def test_put_request_not_found(self, mock_request):
        """ Test GET Not Found """
        mock_request.return_value = mock.MagicMock(spec=Response,
                                                   status_code=404)
        zen = ZenHub('ZENHUB_TOKEN')
        resp = zen.put('/phony', {"message":"ok!"})
        logging.error(resp)
        self.assertIsNone(resp)

    @mock.patch('requests.patch')
    def test_patch_request(self, mock_request):
        """ Test PATCH Request """
        headers = {
            "Content-Length": 17
        }
        mock_request.return_value = mock.MagicMock(spec=Response,
                                                   status_code=200,
                                                   headers=headers)
        mock_request.return_value.json.return_value = {"message":"ok!"}
        zen = ZenHub('ZENHUB_TOKEN')
        resp = zen.patch('/phony', {"message":"ok!"})
        logging.error(resp)
        self.assertEqual(resp['message'], 'ok!')

    @mock.patch('requests.patch')
    def test_patch_not_auth(self, mock_request):
        """ Test PATCH Not Authorized """
        mock_request.return_value = mock.MagicMock(spec=Response,
                                                   status_code=401)
        mock_request.return_value.raise_for_status.side_effect = HTTPError(401)

        zen = ZenHub('ZENHUB_TOKEN')
        self.assertRaises(HTTPError, zen.patch, '/phony', {"message":"ok!"})
