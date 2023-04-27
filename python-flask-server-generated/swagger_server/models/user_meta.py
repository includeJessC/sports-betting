# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserMeta(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, surname: str=None, password: str=None):  # noqa: E501
        """UserMeta - a model defined in Swagger

        :param name: The name of this UserMeta.  # noqa: E501
        :type name: str
        :param surname: The surname of this UserMeta.  # noqa: E501
        :type surname: str
        :param password: The password of this UserMeta.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'name': str,
            'surname': str,
            'password': str
        }

        self.attribute_map = {
            'name': 'name',
            'surname': 'surname',
            'password': 'password'
        }
        self._name = name
        self._surname = surname
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'UserMeta':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserMeta of this UserMeta.  # noqa: E501
        :rtype: UserMeta
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this UserMeta.


        :return: The name of this UserMeta.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this UserMeta.


        :param name: The name of this UserMeta.
        :type name: str
        """

        self._name = name

    @property
    def surname(self) -> str:
        """Gets the surname of this UserMeta.


        :return: The surname of this UserMeta.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        """Sets the surname of this UserMeta.


        :param surname: The surname of this UserMeta.
        :type surname: str
        """

        self._surname = surname

    @property
    def password(self) -> str:
        """Gets the password of this UserMeta.


        :return: The password of this UserMeta.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this UserMeta.


        :param password: The password of this UserMeta.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password