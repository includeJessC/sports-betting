# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RegisterApprove(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, secret_code: str=None):  # noqa: E501
        """RegisterApprove - a model defined in Swagger

        :param id: The id of this RegisterApprove.  # noqa: E501
        :type id: str
        :param secret_code: The secret_code of this RegisterApprove.  # noqa: E501
        :type secret_code: str
        """
        self.swagger_types = {
            'id': str,
            'secret_code': str
        }

        self.attribute_map = {
            'id': 'id',
            'secret_code': 'secret_code'
        }
        self._id = id
        self._secret_code = secret_code

    @classmethod
    def from_dict(cls, dikt) -> 'RegisterApprove':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RegisterApprove of this RegisterApprove.  # noqa: E501
        :rtype: RegisterApprove
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this RegisterApprove.


        :return: The id of this RegisterApprove.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this RegisterApprove.


        :param id: The id of this RegisterApprove.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def secret_code(self) -> str:
        """Gets the secret_code of this RegisterApprove.


        :return: The secret_code of this RegisterApprove.
        :rtype: str
        """
        return self._secret_code

    @secret_code.setter
    def secret_code(self, secret_code: str):
        """Sets the secret_code of this RegisterApprove.


        :param secret_code: The secret_code of this RegisterApprove.
        :type secret_code: str
        """
        if secret_code is None:
            raise ValueError("Invalid value for `secret_code`, must not be `None`")  # noqa: E501

        self._secret_code = secret_code