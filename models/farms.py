#!/usr/bin/env python
"""Module describing the farms table"""
from datetime import datetime
from models.base_model import Base
from sqlalchemy import String, ForeignKey, Table, Column, DateTime
from sqlalchemy.orm  import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from models.products import Produce
    from models.farmers import Farmer
    from models.operations import Operation
    from models.inputs import Input

farm_operation_input = Table(
    "farm_operation_input",
    Base.metadata,
    Column("farm_operation_id", ForeignKey("farm_operation.id", ondelete="CASCADE")),
    Column("input_id", ForeignKey("inputs.id", ondelete="CASCADE"))
)

farm_produce_operation_input = Table(
    "farm_produce_operation_input",
    Base.metadata,
    Column("farm_produce_operation_id", ForeignKey("farm_produce_operation.id", ondelete="CASCADE")),
    Column("input_id", ForeignKey("inputs.id", ondelete="CASCADE"))    
)

class FarmProduceOperation(Base):
    """Liking a farm_produce with operation"""
    __tablename__ = "farm_produce_operation"
    farm_produce_id: Mapped[str] = mapped_column(ForeignKey("farm_produce.id", ondelete="CASCADE"))
    operation_id: Mapped[str] = mapped_column(ForeignKey("operations.id", ondelete="CASCADE"))
    operation_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    inputs: Mapped[List["Input"]] = relationship(secondary=farm_produce_operation_input, back_populates="farm_produce_operations")

    farm_produce: Mapped["FarmProduce"] = relationship(back_populates="operations")
    operation: Mapped["Operation"] = relationship(back_populates="farm_products")

class FarmProduce(Base):
    """Association table connecting farms and products"""
    __tablename__ = "farm_produce"
    farm_id: Mapped[str] = mapped_column(ForeignKey("farms.id", ondelete="CASCADE"))
    produce_id: Mapped[str] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    planting_date: Mapped[datetime] =  mapped_column(DateTime, nullable=False)
    image_file: Mapped[str] = mapped_column(String(128), nullable=False)
    harvest_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    farm: Mapped["Farm"] = relationship(back_populates="products")
    produce: Mapped["Produce"] = relationship(back_populates="farms")
    operations: Mapped[List["FarmProduceOperation"]] = relationship(back_populates="farm_produce")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class FarmOperation(Base):
    """Association table for farms and operations"""
    __tablename__ = "farm_operation"
    farm_id: Mapped[str] = mapped_column(ForeignKey("farms.id", ondelete="CASCADE"))
    operation_id: Mapped[str] = mapped_column(ForeignKey("operations.id", ondelete="CASCADE"))
    operation_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    inputs: Mapped[List["Input"]] = relationship(secondary=farm_operation_input, back_populates="farm_operations")

    farm: Mapped["Farm"] = relationship(back_populates="operations")
    operation: Mapped["Operation"] = relationship(back_populates="farms")

class Farm(Base):
    """Representation of farms"""
    __tablename__ = "farms"
    farm_name: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    address: Mapped[str] = mapped_column(String(128), nullable=False)
    image_file: Mapped[str] = mapped_column(String(128), nullable=True)
    # operations: Mapped[List["Operation"]] = relationship(back_populates="farm")

    farmers: Mapped[List["Farmer"]] = relationship("Farmer", secondary="farmers_farm", back_populates="farms")
    products: Mapped[List["FarmProduce"]] = relationship(back_populates="farm")
    operations: Mapped[List["FarmOperation"]] = relationship(back_populates="farm")

    def __init__(self, *args, **kwargs):
        """initializes farm"""
        super().__init__(*args, **kwargs)
