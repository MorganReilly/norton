"""
user.py

SQLCodegen Generated Database Table: User

This class is autogenerated by SQLCodegen, for use with SQLAlchemy
"""
from swagger_server.__main__ import database
import bcrypt


class User(database.Model):
    """Model for user accounts."""
    __tablename__ = 'user'

    user_id = database.Column(database.INTEGER(), primary_key=True)
    user_name = database.Column(database.String(32), nullable=False, unique=True)
    password = database.Column(database.String(255), nullable=False)
    display_name = database.Column(database.String(32), nullable=False)

    def set_password(self, password):
        """Create hashed password."""
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())

    def check_password(self, password):
        """Check hashed password."""
        return bcrypt.checkpw(password.encode('utf8'), self.password.encode('utf8'))

    def __repr__(self):
        return '<User {}>'.format(self.user_name)
