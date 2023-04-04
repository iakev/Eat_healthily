#!/usr/bin/env python
"""Module describing products"""
from datetime import datetime
from models.base_model import Base
from sqlalchemy import Table, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from models.operations import Operation
    from models.farms import Farm, FarmProduce
    from models.inputs import Input

class Produce(Base):
    """Representation of farm produce"""
    __tablename__ = "products"
    produce_name: Mapped[str] = mapped_column(String(128), nullable=False)
    image_file: Mapped[str] = mapped_column(String(128), nullable=True)

    farms: Mapped[List["FarmProduce"]] = relationship(back_populates="produce")

    def __init__(self, *args, **kwargs):
        """initializes produce"""
        super().__init__(*args, **kwargs)

    
    