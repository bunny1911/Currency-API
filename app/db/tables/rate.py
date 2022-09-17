from datetime import datetime
from sqlalchemy import Column, ForeignKey, INTEGER, NUMERIC, TIMESTAMP
from sqlalchemy.orm import relationship

from ..base import Base
from .currency import Currency


class Rate(Base):
    __tablename__ = "rate"

    id: int = Column(INTEGER, primary_key=True, autoincrement=True)
    currency_id: int = Column(INTEGER, ForeignKey(Currency.id), nullable=False)
    created_at: datetime = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)
    value: float = Column(NUMERIC(10, 4), nullable=False)

    currency: Currency = relationship("Currency", back_populates="rates")
