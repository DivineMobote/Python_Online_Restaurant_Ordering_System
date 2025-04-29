from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    completion_status = Column(String(50), default="pending")
    type = Column(String(50))
    amount = Column(DECIMAL)
    time_paid = Column(DATETIME, default=date.today)

    order_id = Column(Integer, ForeignKey("orders.id"), unique=True)
    order = relationship("Order", back_populates="payments")