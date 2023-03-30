#!/usr/bin/env python
"""Creating the user model that derives from base_model"""
from models.users import User
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Consumer(User):
    """Representation of farmer inheriting from User"""
    __tablename__ = "consumers"
    id: Mapped[str] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)

    __mapper_args__= {
        'polymorphic_identity':'consumer'
    }

    def __init__(self, *args, **kwargs):
        """initializes consumer"""
        super().__init__(*args, **kwargs)

    def authenticate_user(self, login_email, login_password):
        return super().authenticate_user(login_email, login_password)
    