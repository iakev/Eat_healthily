#!/usr/bin.python3
"""Creating the farmer model that derives from base_model"""
from models.base_model import Base
from models.users import User
from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from models.farms import Farm

farmers_farm = Table(
    "farmers_farm",
    Base.metadata,
    Column("farmer_id", ForeignKey("farmers.id", ondelete='CASCADE')),
    Column("farms_id", ForeignKey("farms.id", ondelete='CASCADE'))
)

class Farmer(User):
    """Representation of farmer inheriting from User"""
    __tablename__ = "farmers"
    id: Mapped[str] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    
    farms: Mapped[List["Farm"]] = relationship("Farm", secondary=farmers_farm, back_populates="farmers") 

    __mapper_args__= {
        'polymorphic_identity':'farmer'
    }

    def __init__(self, *args, **kwargs):
        """initializes farmer"""
        super().__init__(*args, **kwargs)

    def authenticate_user(self, login_email, login_password):
        return super().authenticate_user(login_email, login_password)
    