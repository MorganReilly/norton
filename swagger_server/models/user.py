"""
user.py

Swagger Generated User Model

This class is autogenerated by Swagger.
"""
from __future__ import absolute_import
from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int = None, username: str = None, password: str = None,
                 display_name: str = None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param display_name: The display_name of this User.  # noqa: E501
        :type display_name: str
        """
        self.swagger_types = {
            'id': int,
            'username': str,
            'password': str,
            'display_name': str
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'password': 'password',
            'display_name': 'displayName'
        }
        self._id = id
        self._username = username
        self._password = password
        self._display_name = display_name

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> float:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id: float):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this User.

        In the case of user creation the password field will be the plaintext password in all other instances where the server returns a User object it will be a combination of the hash of the users password and associated salt  # noqa: E501

        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.

        In the case of user creation the password field will be the plaintext password in all other instances where the server returns a User object it will be a combination of the hash of the users password and associated salt  # noqa: E501

        :param password: The password of this User.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def display_name(self) -> str:
        """Gets the display_name of this User.


        :return: The display_name of this User.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """Sets the display_name of this User.


        :param display_name: The display_name of this User.
        :type display_name: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name
