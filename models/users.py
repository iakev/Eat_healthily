#!/usr/bin/env python
"""Module defining the user class that all types of user will inherit"""
from hashlib import md5
from models.base_model import Base
from sqlalchemy import String, select
from sqlalchemy.orm import Mapped 
from sqlalchemy.orm import mapped_column


class User(Base):
    """Representation of users"""
    __tablename__ = 'users'
    first_name: Mapped[str] = mapped_column(String(128), nullable=True)
    last_name: Mapped[str] = mapped_column(String(128), nullable=True)
    email: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    phone: Mapped[str] = mapped_column(String(128))
    image_file: Mapped[str] = mapped_column(String(128), nullable=True)
    type: Mapped[str] = mapped_column(String(128))

    __mapper_args__ = {
        'polymorphic_identity':'user',
        'polymorphic_on': type
    }

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self,name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

