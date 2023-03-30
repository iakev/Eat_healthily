#!/usr/bin/env python
"""Describing the input table of the database"""
import enum
from datetime import datetime
from models.base_model import Base
from sqlalchemy import String, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from models.farms import FarmProduceOperation, FarmOperation

class ToxLevels(enum.Enum):
    """my enumerations of toxic levels"""
    level_1_highly_toxic = "Highly toxic"
    level_2_toxic = "Toxic"
    level_3_moderately_toxic = "Moderately toxic"
    level_4_slightly_toxic = "Slightly toxic"
    level_5_non_toxic = "Virtually non-toxic"

class Input(Base):
    """The class that defines inputs to the farm"""
    __tablename__ = "inputs"
    input_name: Mapped[str] = mapped_column(String(128), nullable=False)
    manufactring_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    expiry_data: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    source: Mapped[str] = mapped_column(String(128), nullable=False)
    cautions: Mapped[str] = mapped_column(String(255), nullable=True)
    pre_harvest_interval: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    toxicity_level: Mapped[enum.Enum] = mapped_column(Enum(ToxLevels), nullable=True)
    ingredient: Mapped[str] = mapped_column(String(255), nullable=True)
    image_file_name: Mapped[str] = mapped_column(String(128), nullable=True)
    label_file_name: Mapped[str] = mapped_column(String(128), nullable=True)
    user_manual_file_name: Mapped[str] = mapped_column(String(128), nullable=True)

    # produce_operation_id: Mapped[str] = mapped_column(ForeignKey("produce_operation.id")) 
    # produce_operation: Mapped["ProduceOperation"] = relationship(back_populates="inputs")
    farm_produce_operations: Mapped[List["FarmProduceOperation"]] = relationship(secondary="farm_produce_operation_input", back_populates="inputs")
    farm_operations: Mapped[List["FarmOperation"]] = relationship(secondary="farm_operation_input", back_populates="inputs")
    # farm_operation: Mapped["FarmOperation"] = relationship(back_populates="inputs")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)