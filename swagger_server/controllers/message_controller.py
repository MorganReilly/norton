"""
message_controller.py

OpenAPI Generated Controller: Channel

This class is autogenerated by OpenAPI, for use with SQLAlchemy.
https://github.com/OpenAPITools/openapi-generator
"""
import connexion
from sqlalchemy.exc import SQLAlchemyError
from swagger_server.models.all_messages import AllMessages
from swagger_server.models.message import Message
from ..models.db_models.message import Message as dbMessage


def add_message(body=None):  # noqa: E501
    """Message has been created

    Message has been created # noqa: E501

    :param body: Message to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Message.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_message_by_id(id):  # noqa: E501
    """Deletes an existing message

    Deletes an existing message # noqa: E501

    :param id: The message ID
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_messages():  # noqa: E501
    """Returns all messages

    Returns all messages in a channel # noqa: E501


    :rtype: AllMessages
    """
    try:
        # Query DB
        query = dbMessage.query.all()
        response = []
        for message in query:
            m = Message()
            m.id = message.message_id
            m.channel_id = message.channel_id
            m.user_id = message.user_id
            m.content = message.message_content
            m.timestamp = message.message_timestamp
            m.edited_timestamp = message.edited_timestamp
            response.append(m)

        res = AllMessages.from_dict(response)

        return res, 200
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error


def get_message_by_id(id):  # noqa: E501
    """Get a message by its ID

    Returns a single message if it exists # noqa: E501

    :param id: The message ID
    :type id: int

    :rtype: Message
    """
    return 'do some magic!'


def update_message_by_id(id, body=None):  # noqa: E501
    """Updates an existing message

    Updates an existing message # noqa: E501

    :param id: The message ID
    :type id: int
    :param body: Message to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Message.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
