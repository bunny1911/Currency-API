from typing import TYPE_CHECKING
from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import relationship

from ..base import Base

if TYPE_CHECKING:
    from .rate import Rate


class Currency(Base):
    __tablename__ = "currency"
    
    id: int = Column(INTEGER, primary_key=True, autoincrement=True)
    code: str = Column(VARCHAR(3), unique=True, nullable=False)
    title: str = Column(VARCHAR, nullable=False)

    rates: "list[Rate]" = relationship("Rate", back_populates="currency")
