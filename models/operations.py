#!/usr/bin/env python
"""Module describing operations tracked in produces"""
from datetime import datetime
from models.base_model import Base
from sqlalchemy import String, Column,Table, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from models.farms import FarmOperation, FarmProduceOperation
    from models.inputs import Input


class Operation(Base):
    """Representing operation table"""
    __tablename__ = "operations"
    operation_name: Mapped[str] = mapped_column(String(128), nullable=False)
    # farm_produce_id: Mapped[str] = mapped_column(ForeignKey("farm_produce.id"))
    # farm_id: Mapped[str] = mapped_column(ForeignKey("farms.id"), nullable=True)
    # farm: Mapped["Farm"] = relationship(back_populates="operations")
    # product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), nullable=True)
    # product: Mapped["Produce"] = relationship(back_populates="operations")
    # inputs: Mapped[List["Input"]] = relationship("Input", secondary=operation_input, back_populates="operations")

    farm_products: Mapped[List["FarmProduceOperation"]] = relationship(back_populates="operation")
    farms: Mapped[List["FarmOperation"]] = relationship(back_populates="operation")

    def __init__(self, *args, **kwargs):
        """initializes operations"""
        super().__init__(*args, **kwargs)