"""
| Module: models.py
| Location: eoincode.app
| Purpose: Mdels for demo database
"""
from .extensions import db
from sqlalchemy import Boolean, DateTime, Column, Integer, String

class Testers(db.Model):
    """Stores usernames and passwords resulting from for centra
    website new user testing."""
    __tablename__ = 'testers'
    __table_args__ = {'extend_existing': True}

    user_id = Column(Integer, primary_key=True)
    firstname = Column(String(15))
    lastname = Column(String(15))
    password_str = Column(String(15))
    email = Column(String(40))

    def __init__(self, email, firstname, lastname, password_str):
        """Table record constructer"""
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password_str = password_str

    def __repr__(self):
        """Generic output string for model"""
        return '{}, {}'.format(self.email, self.password)


