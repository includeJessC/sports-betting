# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.bets import Bets  # noqa: F401,E501
from swagger_server import util


class Match(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, first_team_name: str=None, second_team_name: str=None, first_team_result: int=None, second_team_result: int=None, bets_result: float=None, user_bets: List[Bets]=None):  # noqa: E501
        """Match - a model defined in Swagger

        :param id: The id of this Match.  # noqa: E501
        :type id: int
        :param name: The name of this Match.  # noqa: E501
        :type name: str
        :param first_team_name: The first_team_name of this Match.  # noqa: E501
        :type first_team_name: str
        :param second_team_name: The second_team_name of this Match.  # noqa: E501
        :type second_team_name: str
        :param first_team_result: The first_team_result of this Match.  # noqa: E501
        :type first_team_result: int
        :param second_team_result: The second_team_result of this Match.  # noqa: E501
        :type second_team_result: int
        :param bets_result: The bets_result of this Match.  # noqa: E501
        :type bets_result: float
        :param user_bets: The user_bets of this Match.  # noqa: E501
        :type user_bets: List[Bets]
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'first_team_name': str,
            'second_team_name': str,
            'first_team_result': int,
            'second_team_result': int,
            'bets_result': float,
            'user_bets': List[Bets]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'first_team_name': 'first_team_name',
            'second_team_name': 'second_team_name',
            'first_team_result': 'first_team_result',
            'second_team_result': 'second_team_result',
            'bets_result': 'bets_result',
            'user_bets': 'user_bets'
        }
        self._id = id
        self._name = name
        self._first_team_name = first_team_name
        self._second_team_name = second_team_name
        self._first_team_result = first_team_result
        self._second_team_result = second_team_result
        self._bets_result = bets_result
        self._user_bets = user_bets

    @classmethod
    def from_dict(cls, dikt) -> 'Match':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Match of this Match.  # noqa: E501
        :rtype: Match
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Match.


        :return: The id of this Match.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Match.


        :param id: The id of this Match.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Match.


        :return: The name of this Match.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Match.


        :param name: The name of this Match.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def first_team_name(self) -> str:
        """Gets the first_team_name of this Match.


        :return: The first_team_name of this Match.
        :rtype: str
        """
        return self._first_team_name

    @first_team_name.setter
    def first_team_name(self, first_team_name: str):
        """Sets the first_team_name of this Match.


        :param first_team_name: The first_team_name of this Match.
        :type first_team_name: str
        """
        if first_team_name is None:
            raise ValueError("Invalid value for `first_team_name`, must not be `None`")  # noqa: E501

        self._first_team_name = first_team_name

    @property
    def second_team_name(self) -> str:
        """Gets the second_team_name of this Match.


        :return: The second_team_name of this Match.
        :rtype: str
        """
        return self._second_team_name

    @second_team_name.setter
    def second_team_name(self, second_team_name: str):
        """Sets the second_team_name of this Match.


        :param second_team_name: The second_team_name of this Match.
        :type second_team_name: str
        """
        if second_team_name is None:
            raise ValueError("Invalid value for `second_team_name`, must not be `None`")  # noqa: E501

        self._second_team_name = second_team_name

    @property
    def first_team_result(self) -> int:
        """Gets the first_team_result of this Match.


        :return: The first_team_result of this Match.
        :rtype: int
        """
        return self._first_team_result

    @first_team_result.setter
    def first_team_result(self, first_team_result: int):
        """Sets the first_team_result of this Match.


        :param first_team_result: The first_team_result of this Match.
        :type first_team_result: int
        """
        if first_team_result is None:
            raise ValueError("Invalid value for `first_team_result`, must not be `None`")  # noqa: E501

        self._first_team_result = first_team_result

    @property
    def second_team_result(self) -> int:
        """Gets the second_team_result of this Match.


        :return: The second_team_result of this Match.
        :rtype: int
        """
        return self._second_team_result

    @second_team_result.setter
    def second_team_result(self, second_team_result: int):
        """Sets the second_team_result of this Match.


        :param second_team_result: The second_team_result of this Match.
        :type second_team_result: int
        """
        if second_team_result is None:
            raise ValueError("Invalid value for `second_team_result`, must not be `None`")  # noqa: E501

        self._second_team_result = second_team_result

    @property
    def bets_result(self) -> float:
        """Gets the bets_result of this Match.


        :return: The bets_result of this Match.
        :rtype: float
        """
        return self._bets_result

    @bets_result.setter
    def bets_result(self, bets_result: float):
        """Sets the bets_result of this Match.


        :param bets_result: The bets_result of this Match.
        :type bets_result: float
        """

        self._bets_result = bets_result

    @property
    def user_bets(self) -> List[Bets]:
        """Gets the user_bets of this Match.


        :return: The user_bets of this Match.
        :rtype: List[Bets]
        """
        return self._user_bets

    @user_bets.setter
    def user_bets(self, user_bets: List[Bets]):
        """Sets the user_bets of this Match.


        :param user_bets: The user_bets of this Match.
        :type user_bets: List[Bets]
        """

        self._user_bets = user_bets
