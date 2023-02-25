# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.base_user_info import BaseUserInfo  # noqa: E501
from swagger_server.models.competition import Competition  # noqa: E501
from swagger_server.models.create_bet_body import CreateBetBody  # noqa: E501
from swagger_server.models.create_competition_body import CreateCompetitionBody  # noqa: E501
from swagger_server.models.create_match_body import CreateMatchBody  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.match import Match  # noqa: E501
from swagger_server.models.register_approve import RegisterApprove  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server.models.user_meta import UserMeta  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_competitions_get(self):
        """Test case for competitions_get

        
        """
        query_string = [('id', 'id_example')]
        response = self.client.open(
            '/competitions',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_competitions_info_get(self):
        """Test case for competitions_info_get

        
        """
        query_string = [('competition_id', 'competition_id_example'),
                        ('id', 'id_example')]
        response = self.client.open(
            '/competitions_info',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_competitions_info_post(self):
        """Test case for competitions_info_post

        
        """
        query_string = [('competition_id', 'competition_id_example'),
                        ('id', 'id_example')]
        response = self.client.open(
            '/competitions_info',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_bet_post(self):
        """Test case for create_bet_post

        
        """
        body = CreateBetBody()
        query_string = [('id', 'id_example'),
                        ('match_id', 'match_id_example')]
        response = self.client.open(
            '/create/bet',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_competition_post(self):
        """Test case for create_competition_post

        
        """
        body = CreateCompetitionBody()
        query_string = [('id', 'id_example')]
        response = self.client.open(
            '/create/competition',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_match_post(self):
        """Test case for create_match_post

        
        """
        body = CreateMatchBody()
        query_string = [('id', 'id_example'),
                        ('competion_id', 'competion_id_example')]
        response = self.client.open(
            '/create/match',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_match_info_get(self):
        """Test case for match_info_get

        
        """
        query_string = [('match_id', 'match_id_example'),
                        ('id', 'id_example')]
        response = self.client.open(
            '/match_info',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_get(self):
        """Test case for user_get

        
        """
        query_string = [('id', 'id_example')]
        response = self.client.open(
            '/user',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_login_post(self):
        """Test case for user_login_post

        
        """
        body = BaseUserInfo()
        response = self.client.open(
            '/user_login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_put(self):
        """Test case for user_put

        
        """
        body = UserMeta()
        query_string = [('id', 'id_example')]
        response = self.client.open(
            '/user',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_register_approve_post(self):
        """Test case for user_register_approve_post

        
        """
        body = RegisterApprove()
        response = self.client.open(
            '/user_register_approve',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_register_post(self):
        """Test case for user_register_post

        
        """
        body = UserInfo()
        response = self.client.open(
            '/user_register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
