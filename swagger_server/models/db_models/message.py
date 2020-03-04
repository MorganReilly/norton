# coding: utf-8
from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from swagger_server.__main__ import db


class Message(db.Model):
    __tablename__ = 'message'

    message_id = Column(INTEGER(), primary_key=True)
    channel_id = Column(ForeignKey('channel.channel_id'), nullable=False, index=True)
    user_id = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    message_content = Column(String(255), nullable=False)
    message_timestamp = Column(TIMESTAMP, nullable=False,
                               server_default=text("current_timestamp() ON UPDATE current_timestamp()"))
    edited_timestamp = Column(TIMESTAMP, nullable=False,
                              server_default=text("current_timestamp() ON UPDATE current_timestamp()"))

    channel = relationship('Channel')
    user = relationship('User')