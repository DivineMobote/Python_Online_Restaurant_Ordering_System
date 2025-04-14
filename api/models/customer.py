from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    phone = Column(String(20))
    address = Column(String(200))
    is_guest = Column(Boolean, default=False)
    # last_order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    # last_payment_id = Column(Integer, ForeignKey("payments.id"), nullable=True)

    reviews = relationship("Review", back_populates="customer", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")