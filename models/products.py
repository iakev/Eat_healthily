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

# produce_operation_input = Table(
#     "produce_operation_input",
#     Base.metadata,
#     Column("produce_operation_id", ForeignKey("produce_operation.id", ondelete="CASCADE")),
#     Column("input_id", ForeignKey("inputs.id", ondelete="CASCADE"))
# )

# class FarmProduceOperation(Base):
#     """Association table for product and operation"""
#     __tablename__ = "produce_operation"
#     farm_product_id: Mapped[str] = mapped_column(ForeignKey("farm_produce.id", ondelete="CASCADE"))
#     operation_id: Mapped[str] = mapped_column(ForeignKey("operations.id", ondelete="CASCADE"))
#     operation_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
#     description: Mapped[str] = mapped_column(String(255), nullable=True)
#     inputs: Mapped[List["Input"]] = relationship(back_populates="produce_operation")


#     farm_produce: Mapped["Produce"] = relationship(back_populates="operations")
#     operation: Mapped["Operation"] = relationship(back_populates="products")

class Produce(Base):
    """Representation of farm produce"""
    __tablename__ = "products"
    produce_name: Mapped[str] = mapped_column(String(128), nullable=False)
    # planting_date: Mapped[datetime] =  mapped_column(DateTime, nullable=True)
    # harvest_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    # operations: Mapped[List["Operation"]] = relationship(back_populates="product")

    farms: Mapped[List["FarmProduce"]] = relationship(back_populates="produce")

    def __init__(self, *args, **kwargs):
        """initializes produce"""
        super().__init__(*args, **kwargs)

    
    